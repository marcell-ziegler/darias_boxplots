import sys
import tkinter as tk
from tkinter import BooleanVar
from typing import NoReturn

import matplotlib as mpl
from matplotlib.figure import Figure
from widgets import (
    GraphFrame,
    OptionsFrame,
    SaveButton,
    GetPlotDataButton,
)

mpl.use("TkAgg")


class App(tk.Tk):
    plot: Figure = Figure()
    has_grid: tk.BooleanVar

    def __init__(self):
        super().__init__()
        self.has_grid = BooleanVar(value=True)

        self.title("Darias Boxplots")
        self.geometry("1000x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=20)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.graph_frame = GraphFrame(self)
        self.graph_frame.grid(column=0, row=0, sticky="nsew")

        self.file_button = GetPlotDataButton(self)
        self.file_button.grid(column=0, row=1, sticky="nsew")

        self.save_button = SaveButton(self)
        self.save_button.grid(column=0, row=2, sticky="nsew")

        self.options_panel = OptionsFrame(self)
        self.options_panel.grid(column=0, row=3, sticky="nsew", pady=20)

        self.protocol("WM_DELETE_WINDOW", self.stop_app)

    def stop_app(self) -> NoReturn:
        self.destroy()
        sys.exit(0)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
