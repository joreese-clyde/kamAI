import tkinter as tk
from src.core.constants import C

class InfoPanel:

    @staticmethod
    def build(app, parent):

        app.lbl_num_big = tk.Label(
            parent,
            text="—",
            font=("Segoe UI", 72, "bold"),
            fg=C["text_dim"],
            bg=C["surface"],
        )
        app.lbl_num_big.pack()

    @staticmethod
    def set_number(app, num: int):
        words = app.T.get("num_words", {})
        if num in words:
            text = words[num]
        else:
            text = "—"

        app.lbl_num_big.config(text=text)

