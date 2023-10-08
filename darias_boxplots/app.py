import sys
import tkinter as tk
from tkinter import BooleanVar
from typing import NoReturn

import matplotlib as mpl
from matplotlib.figure import Figure
from darias_boxplots.widgets import widgets as w

mpl.use("TkAgg")


class App(tk.Tk):
    plot: Figure = Figure()

    def __init__(self):
        super().__init__()
        self.has_grid = BooleanVar(value=True)

        self.title("Darias Boxplots")
        self.geometry("1000x600")
        # self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.plot_panel = w.PlotPanel(self, self.plot, borderwidth=2, relief="groove")
        self.plot_panel.grid(column=0, row=0, sticky="nsew")

        self.options_panel = w.OptionsPanel(
            self, self.plot, borderwidth=2, relief="groove"
        )
        self.options_panel.grid(column=1, row=0, sticky="nsew")

        self.protocol("WM_DELETE_WINDOW", self.stop_app)

    def stop_app(self) -> NoReturn:
        self.destroy()
        sys.exit(0)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
