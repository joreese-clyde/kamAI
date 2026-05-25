import tkinter as tk
from src.core.constants import C


class Header:

    @staticmethod
    def build(app, parent):

        bar = tk.Frame(parent, bg=C["surface"], height=60)
        bar.pack(fill="x")

        # LEFT SIDE
        title = tk.Label(
            bar,
            text=app.T["app_title"],
            font=("Segoe UI", 16, "bold"),
            fg=C["text"],
            bg=C["surface"]
        )

        title.pack(side="left", padx=20)

        # RIGHT SIDE
        controls = tk.Frame(bar, bg=C["surface"])
        controls.pack(side="right", padx=20)

        # LANGUAGE BUTTON
        app.btn_lang = tk.Button(
            controls,
            text=app.T["btn_lang"],
            bg=C["surface2"],
            fg=C["text"],
            relief="flat",
            cursor="hand2",
            command=app._toggle_lang
        )

        app.btn_lang.pack(side="right", padx=5)

        # START CAMERA BUTTON
        app.btn_cam = tk.Button(
            controls,
            text=app.T["btn_start"],
            bg=C["accent"],
            fg="black",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
            command=app._toggle_camera
        )


        app.btn_cam.pack(side="right", padx=5)