from copy import copy
import sys
from typing import NoReturn
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk

mpl.use("TkAgg")


class GraphFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas = FigureCanvasTkAgg(self.master.plot, self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


class GetPlotDataButton(ttk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent, text="Get Plot Data", command=self.set_plot_object, **kwargs
        )

    def set_plot_object(self) -> None:
        filename: str = askopenfilename(filetypes=[("Data Files", ("*.csv", "*.txt"))])

        with open(filename, "r", encoding="utf8") as f:
            raw_data = f.read()

            if ",;" not in raw_data:
                data = np.fromstring(raw_data, sep="\n")
            else:
                data = np.fromstring(raw_data, sep="," if "," in raw_data else ";")
        fig, ax = plt.subplots()
        ax.boxplot(data, vert=False)

        ax.get_yaxis().set_visible(False)
        ax.grid(True)

        self.master.plot = copy(fig)
        self.master.graph_frame.grid_forget()
        self.master.graph_frame = GraphFrame(self.master)
        self.master.graph_frame.grid(column=0, row=0, sticky="nsew")
        # print("Updated plot object")


class SaveButton(ttk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Save Plot", command=self.save_plot, **kwargs)

    def save_plot(self) -> None:
        filename: str = asksaveasfilename(filetypes=[("PNG", "*.png")])
        self.master.plot.savefig(filename, backend="AGG")


class App(tk.Tk):
    plot: Figure = Figure()

    def __init__(self):
        super().__init__()
        self.title("Darias Boxplots")
        self.geometry("800x600")
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

        self.protocol("WM_DELETE_WINDOW", self.stop_app)

    def stop_app(self) -> NoReturn:
        self.destroy()
        sys.exit(0)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
