import tkinter as tk
import threading
import time
import cv2

from PIL import Image, ImageTk

from src.core.language import LANG
from src.core.constants import C
from src.core.hand_tracker import FingerCounter

from src.ui.header import Header
from src.ui.camera_panel import CameraPanel
from src.ui.info_panel import InfoPanel
from src.ui.statusbar import StatusBar


class HandSignApp:

    APP_W = 1180
    APP_H = 760

    def __init__(self):

        # LANGUAGE
        self.lang_key = "en"
        self.T = LANG[self.lang_key]

        # CAMERA
        self.running = False
        self.cap = None
        self.counter = None
        self.thread = None

        # FRAME DATA
        self._last_frame = None
        self._cur_num = -1
        self._num_hands = 0
        self._fps = 0.0
        self._conf = 0.0
        self._prev_time = 0.0

        # TKINTER
        self.root = tk.Tk()
        self.root.title("kamAI")
        self.root.configure(bg=C["bg"])

        self._configure_window()
        self._build_ui()

    # -------------------------------------------------
    # WINDOW
    # -------------------------------------------------

    def _configure_window(self):

        self.root.geometry(
            f"{self.APP_W}x{self.APP_H}"
        )

        self.root.resizable(False, False)

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self._on_close
        )

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def _build_ui(self):

        Header.build(self, self.root)

        content = tk.Frame(
            self.root,
            bg=C["bg"]
        )

        content.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # LEFT PANEL
        left = tk.Frame(
            content,
            bg=C["bg"]
        )

        left.pack(
            side="left",
            fill="both",
            expand=True
        )

        # RIGHT PANEL
        right = tk.Frame(
            content,
            bg=C["surface"],
            width=320
        )

        right.pack(
            side="right",
            fill="y",
            padx=(15, 0)
        )

        right.pack_propagate(False)

        # BUILD COMPONENTS
        CameraPanel.build(self, left)
        InfoPanel.build(self, right)
        StatusBar.build(self, self.root)

    # -------------------------------------------------
    # LANGUAGE
    # -------------------------------------------------

    def _toggle_lang(self):

        self.lang_key = (
            "tl"
            if self.lang_key == "en"
            else "en"
        )

        self.T = LANG[self.lang_key]

        # UPDATE LANGUAGE BUTTON
        if hasattr(self, "btn_lang"):

            self.btn_lang.config(
                text=self.T.get(
                    "btn_lang",
                    "Language"
                )
            )

        # UPDATE CAMERA BUTTON
        if hasattr(self, "btn_cam"):

            if self.running:

                self.btn_cam.config(
                    text=self.T.get(
                        "btn_stop",
                        "Stop Camera"
                    )
                )

            else:

                self.btn_cam.config(
                    text=self.T.get(
                        "btn_start",
                        "Start Camera"
                    )
                )

    # -------------------------------------------------
    # CAMERA CONTROL
    # -------------------------------------------------

    def _toggle_camera(self):

        if self.running:
            self._stop_camera()
        else:
            self._start_camera()

    def _start_camera(self):

        # OPEN CAMERA
        self.cap = cv2.VideoCapture(
            0,
            cv2.CAP_DSHOW
        )

        # CAMERA CHECK
        if not self.cap.isOpened():

            print("Camera not found")
            return

        # CAMERA SIZE
        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            640
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            480
        )

        # HAND TRACKER
        self.counter = FingerCounter()

        # RUNNING
        self.running = True

        # BUTTON UPDATE
        if hasattr(self, "btn_cam"):

            self.btn_cam.config(
                text=self.T.get(
                    "btn_stop",
                    "Stop Camera"
                ),
                bg=C.get(
                    "red",
                    "#ff4d4d"
                )
            )

        # THREAD
        self.thread = threading.Thread(
            target=self._capture_loop,
            daemon=True
        )

        self.thread.start()

        # START FRAME LOOP
        self._poll_frame()

    def _stop_camera(self):

        self.running = False

        # RELEASE CAMERA
        if self.cap:

            self.cap.release()
            self.cap = None

        # RELEASE MEDIAPIPE
        if self.counter:

            self.counter.release()
            self.counter = None

        # CLEAR LAST FRAME
        self._last_frame = None

        # BUTTON RESET
        if hasattr(self, "btn_cam"):

            self.btn_cam.config(
                text=self.T.get(
                    "btn_start",
                    "Start Camera"
                ),
                bg=C["accent"]
            )

        # CLEAR CANVAS
        if hasattr(self, "cam_canvas"):

            self.cam_canvas.delete("all")

    # -------------------------------------------------
    # CAPTURE LOOP
    # -------------------------------------------------

    def _capture_loop(self):

        while self.running:

            # CAMERA CHECK
            if self.cap is None:
                break

            # READ FRAME
            ret, frame = self.cap.read()

            if not ret:
                continue

            # MIRROR EFFECT
            frame = cv2.flip(frame, 1)

            # FPS
            now = time.time()

            if self._prev_time != 0:

                time_delta = (
                    now - self._prev_time
                )

                if time_delta > 0:
                    self._fps = (
                        1 / time_delta
                    )

            self._prev_time = now

            # PROCESS HANDS
            try:

                num, hands, conf, annotated = (
                    self.counter.process(frame)
                )

                self._cur_num = num
                self._num_hands = hands
                self._conf = conf

                self._last_frame = annotated

            except Exception as e:

                print(
                    "Hand tracking error:",
                    e
                )

            # REDUCE CPU USAGE
            time.sleep(0.01)

    # -------------------------------------------------
    # FRAME DISPLAY
    # -------------------------------------------------

    def _poll_frame(self):

        if not self.running:
            return

        frame = self._last_frame

        if frame is not None:

            try:

                # UPDATE NUMBER
                if hasattr(
                    self,
                    "lbl_num_big"
                ):

                    InfoPanel.set_number(
                        self,
                        self._cur_num
                    )

                # BGR -> RGB
                frame = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                # PIL IMAGE
                img = Image.fromarray(
                    frame
                )

                # RESIZE
                img = img.resize(
                    (640, 480)
                )

                # TK IMAGE
                self.cam_img = (
                    ImageTk.PhotoImage(img)
                )

                # DRAW FRAME
                self.cam_canvas.delete(
                    "all"
                )

                self.cam_canvas.create_image(
                    0,
                    0,
                    anchor="nw",
                    image=self.cam_img
                )

            except Exception as e:

                print(
                    "Frame display error:",
                    e
                )

        # LOOP
        self.root.after(
            30,
            self._poll_frame
        )

    # -------------------------------------------------
    # CLOSE
    # -------------------------------------------------

    def _on_close(self):

        self.running = False

        if self.cap:

            self.cap.release()
            self.cap = None

        if self.counter:

            self.counter.release()
            self.counter = None

        self.root.destroy()

    # -------------------------------------------------
    # RUN
    # -------------------------------------------------

    def run(self):

        self.root.mainloop()


# -------------------------------------------------
# START APP
# -------------------------------------------------

if __name__ == "__main__":

    app = HandSignApp()
    app.run()