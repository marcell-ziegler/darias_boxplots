from copy import copy
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as mpl
import pandas as pd

mpl.use("TkAgg")


class HeaderFrame(ttk.Frame):
    graph_title: tk.StringVar
    font_type: tk.StringVar

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Entry for Graph Title
        self.title_entry_label = ttk.Label(self, text="Rubrik")
        self.graph_title = tk.StringVar(value="Grafens rubrik")
        self.title_entry = ttk.Entry(self, textvariable=self.graph_title)
        self.title_entry_label.grid(column=0, row=0, sticky="sw")
        self.title_entry.grid(column=0, row=1, sticky="nsew")

        # Font Selector
        self.font_label = ttk.Label(self, text="Typsnitt")
        self.font_label.grid(column=1, row=0, sticky="sw")

        self.font_selector_frame = ttk.Frame(self)
        self.font_type = tk.StringVar(value="sans-serif")
        self.serif_button = ttk.Radiobutton(
            self.font_selector_frame,
            variable=self.font_type,
            value="serif",
            text="Serif",
        )
        self.sans_serif_button = ttk.Radiobutton(
            self.font_selector_frame,
            variable=self.font_type,
            value="sans-serif",
            text="Sans-serif",
        )
        self.serif_button.grid(column=0, row=0, sticky="nsew")
        self.sans_serif_button.grid(column=1, row=0, sticky="nsew")
        self.font_selector_frame.columnconfigure(0, weight=1)
        self.font_selector_frame.columnconfigure(1, weight=1)
        self.font_selector_frame.rowconfigure(0, weight=1)
        self.font_selector_frame.grid(column=1, row=1, sticky="nsew")


class SettingsFrame(ttk.Frame):
    has_grid: tk.BooleanVar
    length_unit: tk.StringVar
    length_unit_options = (
        "cm",
        "mm",
        "m",
    )

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Section Label
        self.settings_label = ttk.Label(self, text="Inställningar")
        self.settings_label.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=5)

        # Grid Checkbox
        self.has_grid = tk.BooleanVar(value=True)
        self.grid_button = ttk.Checkbutton(
            self, text="Grid", variable=self.has_grid, onvalue=True, offvalue=False
        )
        self.grid_button.grid(column=0, row=1, sticky="nsew")

        # Unit Selector
        self.unit_selector_frame = ttk.Frame(self)
        self.unit_selector_frame.columnconfigure(0, weight=1)
        self.unit_selector_frame.columnconfigure(1, weight=2)

        self.length_unit_label = ttk.Label(self.unit_selector_frame, text="Längdenhet")
        self.length_unit_label.grid(column=0, row=0, sticky="w")
        self.length_unit = tk.StringVar(value="cm")
        self.length_unit_selector = ttk.Combobox(
            self.unit_selector_frame,
            values=self.length_unit_options,
            textvariable=self.length_unit,
        )
        self.length_unit_selector.grid(column=1, row=0, sticky="nsew")


class OptionsPanel(ttk.Frame):
    figure_object: Figure

    def __init__(self, parent, figure: Figure, **kwargs):
        super().__init__(parent, **kwargs)
        self.columnconfigure(0, weight=1)

        self.figure_object = figure

        # Import Button
        self.file_button_frame = ttk.Frame(self, borderwidth=2, relief="groove")
        self.file_button_frame.grid(column=0, row=0, sticky="nsew")
        self.file_button_frame.columnconfigure(0, weight=1)
        self.file_button_frame.rowconfigure(0, weight=1)
        self.file_button = GetPlotDataButton(self.file_button_frame, figure)
        self.file_button.grid(column=0, row=0, sticky="nsew")

        # Frame for Header Settings
        self.header_frame = HeaderFrame(self, borderwidth=2, relief="groove")
        self.header_frame.grid(column=0, row=1, sticky="nsew")

        # Frame for Settings
        self.settings_frame = SettingsFrame(self, borderwidth=2, relief="groove")
        self.settings_frame.grid(column=0, row=2, sticky="nsew")


class PlotPanel(ttk.Frame):
    figure_object: Figure

    def __init__(self, parent, figure: Figure, **kwargs):
        super().__init__(parent, **kwargs)

        self.figure_object = figure

        self.rowconfigure(0, weight=10)
        self.rowconfigure(1, weight=1)

        self.graph_frame = GraphFrame(self, figure)
        self.graph_frame.grid(column=0, row=0, sticky="nsew")
        self.save_button = SaveButton(self, figure)
        self.save_button.grid(column=0, row=1, sticky="nsew", pady=10)


class GraphFrame(ttk.Frame):
    def __init__(self, parent, figure, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


class GetPlotDataButton(ttk.Button):
    figure_object: Figure

    def __init__(self, parent, figure: Figure, **kwargs):
        super().__init__(
            parent, text="Get Plot Data", command=self.set_plot_object, **kwargs
        )
        self.figure_object = figure

    def set_plot_object(self) -> None:
        filename: str = askopenfilename(filetypes=[("Excel files", ("*xlsx"))])

        data = pd.read_excel(filename)
        print(data)


class SaveButton(ttk.Button):
    figure_object: Figure

    def __init__(self, parent, figure: Figure, **kwargs):
        super().__init__(parent, text="Save Plot", command=self.save_plot, **kwargs)
        self.figure_object = figure

    def save_plot(self) -> None:
        filename: str = asksaveasfilename(filetypes=[("PNG", "*.png")])
        self.figure_object.savefig(filename, backend="AGG")
