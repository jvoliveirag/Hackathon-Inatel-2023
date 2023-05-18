"""
Module containing the "TkinterUI" Class.
TODO: FIX THIS MODULE
"""

# from typing import Dict
from tkinter import filedialog, Canvas

import customtkinter
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from .functions import functions
from ...interfaces import UI


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
matplotlib.use('TkAgg')


class TkinterUI(UI, customtkinter.CTk):
    """
    Class to represent a "Tkinter" UserInterface.
    """

    def execute(self) -> None:
        """"""
        self._create_interface()
        self.mainloop()

    def _read_network_traffic_data(self) -> None:
        """
        Private Method to read the network traffic data from the backend.
        """
        self._frm_charts.clipboard_clear()

        traffic_data = functions.read_network_traffic_data()
        names = traffic_data.keys()
        speeds = traffic_data.values()

        # create a figure
        CHART_LENGTH = 10
        CHART_WIDTH = 8
        CHART_SIZE = (CHART_LENGTH, CHART_WIDTH)
        figure = Figure(figsize=CHART_SIZE, dpi=100)
        figure.clear()

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self._frm_charts)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(names, speeds)
        axes.set_title('Speed')
        axes.set_ylabel('Download | Upload')

        figure_canvas.get_tk_widget().grid(row=1)

    def _create_interface(self) -> None:
        """"""
        self._setup()
        self._main_frame_setup()
        self._create_frames()

    def _setup(self) -> None:
        """"""
        self.title("NTracker")
        self.attributes('-zoomed', True)

        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_frames(self) -> None:
        """"""
        self._create_options_frame()
        self._create_charts_frame()
        self._create_tools_frame()

    def _main_frame_setup(self) -> None:
        """"""
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _create_options_frame(self) -> None:
        """"""
        # configure grid layout (1x11)
        frm_options = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        frm_options.grid(row=0, column=0, pady=10, padx=10, sticky="ns")

        frm_options.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(1, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(2, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(3, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(4, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(5, weight=1)    # empty row as spacing
        frm_options.grid_rowconfigure(6, minsize=10)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(7, minsize=20)  # empty row with minsize as spacing

        lbl_options = customtkinter.CTkLabel(
            master=frm_options,
            text="OPTIONS",
            font=("Roboto Medium", 20) # font name and size in px
        )
        lbl_options.grid(row=0, column=0, pady=10, padx=10)

        btn_save_image = customtkinter.CTkButton(
            master=frm_options,
            text="Save Chart",
            command=functions.save_chart
        )
        btn_save_image.grid(row=2, column=0, pady=10, padx=20)

        btn_reset_image = customtkinter.CTkButton(
            master=frm_options,
            text="Export Chart",
            command=functions.export_chart
        )
        btn_reset_image.grid(row=3, column=0, pady=10, padx=20)

        lbl_space = customtkinter.CTkLabel(master=frm_options, text="")
        lbl_space.grid(row=5, column=0)

        lbl_mode = customtkinter.CTkLabel(master=frm_options, text="Appearance Mode:")
        lbl_mode.grid(row=6, column=0, pady=0, padx=20)

        mnu_appearance = customtkinter.CTkOptionMenu(
            master=frm_options,
            values=["Dark", "Light", "System"],
            command=self._change_appearance_mode
        )
        mnu_appearance.grid(row=7, column=0, pady=(0,20), padx=20)
        mnu_appearance.set("Dark")

    def _create_charts_frame(self) -> None:
        """
        Private Method to create the Charts Frame
        """
        self._frm_charts = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        self._frm_charts.grid(row=0, column=1, pady=10, padx=10, sticky="nswe")

        self._frm_charts.grid_rowconfigure(2, minsize=100)

        lbl_image = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="CHARTS",
            font=("Roboto Medium", 20) # font name and size in px
        )
        lbl_image.grid(column=0, row=0, padx=10, pady=10)

        self.canvas = Canvas(self._frm_charts, bg="#2A2D2E", highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nswe")

        self._frm_charts.grid_rowconfigure(1, weight=1)
        self._frm_charts.grid_columnconfigure(0, weight=1)

        btn_get_traffic_data = customtkinter.CTkButton(
            master=self._frm_charts,
            text="Read Network Traffic",
            font=("Roboto Medium", 20),
            height=30,
            width=55,
            border_spacing=20,
            command=self._read_network_traffic_data,
        )
        btn_get_traffic_data.grid(row=2, column=0)

    def _create_tools_frame(self) -> None:
        """"""
        frm_tools = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        frm_tools.grid(row=0, column=2, pady=10, padx=10, sticky="ns")

        lbl_rotate = customtkinter.CTkLabel(
            master=frm_tools,
            text="TOOLS",
            font=("Roboto Medium", 20) # font name and size in px
        )
        lbl_rotate.grid(row=0, column=0, padx=20, pady=10)

        lbl_rotate = customtkinter.CTkLabel(
            master=frm_tools,
            text="Read Network",
            font=("Roboto Medium", 16),
            fg_color=("white", "gray38"),
            corner_radius=5
        )
        lbl_rotate.grid(row=1, column=0)

    def _change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def _on_closing(self):
        """"""
        self.destroy()
