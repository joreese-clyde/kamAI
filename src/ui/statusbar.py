import tkinter as tk
from src.core.constants import C

class StatusBar:

    @staticmethod
    def build(app, parent):

        bar = tk.Frame(parent, bg=C["surface2"], height=28)
        bar.pack(fill="x", side="bottom")

        app.lbl_status = tk.Label(
            bar,
            text="Ready | credits seiko.dev",
            font=("Segoe UI", 10),
            fg=C["text_muted"],
            bg=C["surface2"],
        )

        app.lbl_status.pack(side="left", padx=12)