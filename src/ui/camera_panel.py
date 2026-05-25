import tkinter as tk
from src.core.constants import C

class CameraPanel:

    @staticmethod
    def build(app, parent):

        card = tk.Frame(parent, bg=C["surface"])
        card.pack(fill="both", expand=True)

        app.cam_canvas = tk.Canvas(
            card,
            width=640,
            height=480,
            bg=C["cam_bg"],
            highlightthickness=0,
        )

        app.cam_canvas.pack(padx=12, pady=12)