"""
Module containing the "TkinterUI" Class.
TODO: FIX THIS MODULE
"""

import json
import tkinter as tk

import customtkinter
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from .functions import functions
from ...interfaces import UI


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
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
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_options.grid(row=0, column=0, pady=10, padx=10)

        btn_save_chart = customtkinter.CTkButton(
            master=frm_options,
            text="Save Data",
            command=self._save_chart
        )
        btn_save_chart.grid(row=2, column=0, pady=10, padx=20)

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

        lbl_chart_title = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="CHARTS",
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_chart_title.grid(column=0, row=0, padx=10, pady=10)

        self._frm_charts.grid_rowconfigure(1, weight=1)
        self._frm_charts.grid_columnconfigure(0, weight=1)

        frm_buttons = customtkinter.CTkFrame(master=self._frm_charts)
        frm_buttons.grid(row=2, column=0)

        btn_get_traffic_data = customtkinter.CTkButton(
            master=frm_buttons,
            text="Read Network Traffic",
            font=("Roboto Medium", 20),
            border_spacing=20,
            command=self._read_network_traffic_data,
        )
        btn_get_traffic_data.grid(row=0, column=0)

        # Insert an empty spacer frame for spacing
        lbl_space= customtkinter.CTkLabel(master=frm_buttons, text="", width=80, bg_color=frm_buttons["bg"])
        lbl_space.grid(row=0, column=1, sticky="nswe")

        btn_get_traffic_speed_average = customtkinter.CTkButton(
            master=frm_buttons,
            text="Read Network Traffic Average Speed",
            font=("Roboto Medium", 20),
            border_spacing=20,
            command=self._read_network_traffic_average_speed,
        )
        btn_get_traffic_speed_average.grid(row=0, column=2)

    def _read_network_traffic_average_speed(self) -> None:
        """
        TODO
        """
        self._clear_screen()

        lbl_loading_message = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="Please wait while we read your traffic network...",
            font=("Roboto Medium", 20)
        )
        lbl_loading_message.grid(row=1, column=0)
        self._frm_charts.update()

        self._frm_charts.grid_rowconfigure(1, weight=1)
        self._frm_charts.grid_columnconfigure(0, weight=1)

        average_speeds = functions.read_network_traffic_average_speed()

        names = average_speeds.keys()
        speeds = average_speeds.values()

        download_speeds = [speed['download'] for speed in speeds]
        upload_speeds = [speed['upload'] for speed in speeds]

        x_positions = range(len(names))

        # create a figure
        CHART_LENGTH = 18
        CHART_WIDTH = 8
        CHART_SIZE = (CHART_LENGTH, CHART_WIDTH)
        figure = Figure(figsize=CHART_SIZE, dpi=100, facecolor='#2B2B2B')
        figure.clear()

        # create FigureCanvasTkAgg object
        self._figure_canvas = FigureCanvasTkAgg(figure, self._frm_charts)

        # create axes
        axes = figure.add_subplot(facecolor='#2B2B2B')

        # Assign colors to the bars
        download_color = '#494f56'
        upload_color = '#0f0'

        # create the barcharts for download and upload speeds
        axes.bar(x_positions, download_speeds, label='Download', color=download_color)
        axes.bar(x_positions, upload_speeds, label='Upload', bottom=download_speeds, color=upload_color)
        axes.set_title('Average Speed (B/s)', color='white')
        axes.set_ylabel('Download | Upload', color='white')
        axes.set_xticks(x_positions)
        axes.set_xticklabels(names, color='white')
        axes.legend()

        lbl_loading_message.destroy()

        self._figure_canvas.get_tk_widget().grid(row=1)

    def _read_network_traffic_data(self) -> None:
        """
        Private Method to read the network traffic data from the backend.
        """
        self._clear_screen()

        traffic_data = functions.read_network_traffic_data()

        self._scrollbar = tk.Scrollbar(self._frm_charts)
        self._scrollbar.grid(row=1, column=1, sticky="ns")

        self._text_widget = tk.Text(self._frm_charts, wrap="word", bg=self["bg"], fg="#0f0")
        self._text_widget.grid(row=1, column=0, sticky="nswe")
        self._text_widget.config(yscrollcommand=self._scrollbar.set)
        

        self._scrollbar.config(command=self._text_widget.yview)

        formatted_json = json.dumps(traffic_data, indent=4, sort_keys=True)
        self._text_widget.insert("1.0", formatted_json)
        self._text_widget.config(state='disabled')

    def _save_chart(self):
        """
        TODO
        """
        if not hasattr(self, "_figure_canvas"):
            tk.messagebox.showerror("Error", 'No chart to save. Try to create a chart first by using button "Read Network Traffic Average Speed".')
            return

        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])

        if file_path:
            self._figure_canvas.print_png(file_path)

    def _clear_screen(self) -> None:
        """
        TODO
        """
        if hasattr(self, "_text_widget"):
            self._text_widget.destroy()

        if hasattr(self, "_scrollbar"):
            self._scrollbar.destroy()

        if hasattr(self, "_figure_canvas"):
            self._figure_canvas.get_tk_widget().destroy()

        # for widget in self._frm_charts.winfo_children():
        #     widget.destroy()

    def _change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def _on_closing(self):
        """"""
        self.destroy()
