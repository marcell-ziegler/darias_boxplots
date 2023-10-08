from copy import copy
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as mpl

mpl.use("TkAgg")


class GraphFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas = FigureCanvasTkAgg(self.master.plot, self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


class OptionsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.grid_checkbox = ttk.Checkbutton(
            self,
            text="Grid",
            variable=self.master.has_grid,
            onvalue=True,
            offvalue=False,
        )
        self.grid_checkbox.grid(column=0, row=0)


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
        ax.grid(self.master.has_grid.get())

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
