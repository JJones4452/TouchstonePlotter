"""Jake Jones (C) 2022 - GPL-3 Licence 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. """


import matplotlib.pyplot as plt
import skrf as rf
import os, sys
from enum import Enum

class S_Parameter(Enum):
    S11 = 1
    S12 = 2
    S13 = 3
    S14 = 4

    S21 = 5
    S22 = 6
    S23 = 7
    S24 = 8

    S31 = 9
    S32 = 10
    S33 = 11
    S34 = 12

    S41 = 13
    S42 = 14
    S43 = 15
    S44 = 16

class Frequency_Unit(Enum):
    Hz = 1
    kHz = 2
    MHz = 3
    GHz = 4
    THz = 5

class TouchStonePlotter:
    def __init__(self, folder_path: str, type_file_wanted: str) -> None:
        self.folder_path: str = folder_path
        self.type_file_wanted: str = type_file_wanted
        pass

    
    def find_all_sxp_files(self) -> list[str]:
        """Finds all files in the directory with the extension specified in the 'type_file_wanted' string. 
        Is not recursive so only looks in the directory specified. Returns list of found files."""
        if(not os.path.exists(self.folder_path)):
            print("Error: Path is invalid")
            return
        all_files_in_direc: list[str] = os.listdir(self.folder_path)
        
        return [(str.format("{}/{}", self.folder_path, file )) for file in all_files_in_direc if (self.type_file_wanted in file)]

    def select_file_to_use(self, all_files: list[str] , fn_to_use: str) -> str:
        found_file: list[str] = [x for x in all_files if (fn_to_use in x)]
        if(len(found_file) > 0):
            return found_file[0]
        else:
            print("File Not Found")
            return None

    def get_s_param_text_for_legend(self, s_param: S_Parameter) -> str:
        match s_param:
            case S_Parameter.S11:
                return "$S_{11}$"
            case S_Parameter.S12:
                return "$S_{12}$"
            case S_Parameter.S13:
                return "$S_{13}$"
            case S_Parameter.S14:
                return "$S_{14}$"
            case S_Parameter.S21:
                return "$S_{21}$"
            case S_Parameter.S22:
                return "$S_{22}$"
            case S_Parameter.S23:
                return "$S_{23}$"
            case S_Parameter.S24:
                return "$S_{24}$"
            case S_Parameter.S31:
                return "$S_{31}$"
            case S_Parameter.S32:
                return "$S_{32}$"
            case S_Parameter.S33:
                return "$S_{33}$"
            case S_Parameter.S34:
                return "$S_{34}$"
            case S_Parameter.S41:
                return "$S_{41}$"
            case S_Parameter.S42:
                return "$S_{42}$"
            case S_Parameter.S43:
                return "$S_{43}$"
            case S_Parameter.S44:
                return "$S_{44}$"

    def get_frequency_text(self, freq_enum: Frequency_Unit) -> dict[int, str]:
        match(freq_enum):
            case Frequency_Unit.Hz:
                return {1 : "Hz", 2 : "hz"}
            case Frequency_Unit.kHz:
                return {1 : "kHz", 2 : "khz"}
            case Frequency_Unit.MHz:
                return {1 : "MHz", 2 : "mhz"}
            case Frequency_Unit.GHz:
                return {1 : "GHz", 2 : "ghz"}
            case Frequency_Unit.THz:
                return {1 : "THz", 2 : "thz"}

    def plot_s_param(self, curr_network_file: rf.Network, s_param: S_Parameter, legend_text: str) -> None:
        match s_param:
            case S_Parameter.S11:
                curr_network_file.s11.plot_s_db(label = legend_text)
            case S_Parameter.S12:
                curr_network_file.s12.plot_s_db(label = legend_text)
            case S_Parameter.S13:
                curr_network_file.s13.plot_s_db(label = legend_text)
            case S_Parameter.S14:
                curr_network_file.s14.plot_s_db(label = legend_text)
            case S_Parameter.S21:
                curr_network_file.s21.plot_s_db(label = legend_text)
            case S_Parameter.S22:
                curr_network_file.s22.plot_s_db(label = legend_text)
            case S_Parameter.S23:
                curr_network_file.s23.plot_s_db(label = legend_text)
            case S_Parameter.S24:
                curr_network_file.s24.plot_s_db(label = legend_text)
            case S_Parameter.S31:
                curr_network_file.s31.plot_s_db(label = legend_text)
            case S_Parameter.S32:
                curr_network_file.s32.plot_s_db(label = legend_text)
            case S_Parameter.S33:
                curr_network_file.s33.plot_s_db(label = legend_text)
            case S_Parameter.S34:
                curr_network_file.s34.plot_s_db(label = legend_text)
            case S_Parameter.S41:
                curr_network_file.s41.plot_s_db(label = legend_text)
            case S_Parameter.S42:
                curr_network_file.s42.plot_s_db(label = legend_text)
            case S_Parameter.S43:
                curr_network_file.s43.plot_s_db(label = legend_text)
            case S_Parameter.S44:
                curr_network_file.s44.plot_s_db(label = legend_text)


    def change_legend_text(self, list_of_text_for_legend: list[str]) -> None:
        plt.legend(labels = list_of_text_for_legend)

    def show_plot(self) -> None:
        plt.show()

    def set_plot_title(self, title: str) -> None:
        plt.title(title)

    def plot_parameter(self, 
                            file_to_plot: str, 
                            s_param_to_plot: S_Parameter, 
                            legend_text: str, 
                            y_axis_label: str = "Magnitude (dB)", 
                            frequency_unit: Frequency_Unit = Frequency_Unit.Hz,
                            do_show: bool = False
                            ) -> None:
        s_param_file: rf.Network = rf.Network(file_to_plot)
        unit_str: str = self.get_frequency_text(frequency_unit)
        x_label: str = f"Frequency ({unit_str[1]})"

        s_param_file.frequency.unit = f'{unit_str[2]}'
        self.plot_s_param(s_param_file, s_param_to_plot, legend_text)
        
        plt.xlabel(xlabel=fr"${x_label}$")
        plt.ylabel(ylabel=fr"${y_axis_label}$")
        
        if(do_show):
            plt.show()

    def plot_multiple_on_one_graph(self, params_per_file: dict[str, list[S_Parameter]], frequency_unit: Frequency_Unit = Frequency_Unit.Hz) -> None:
        for key, value in params_per_file.items():
            for sparam in value:
                legend_txt: str = self.get_s_param_text_for_legend(s_param=sparam)
                self.plot_parameter(key, sparam, legend_txt, frequency_unit=frequency_unit)
        plt.tight_layout()
        plt.grid(visible=True)

if __name__ == "__main__":
    k = TouchStonePlotter(r"", ".s2p")
    gg = k.find_all_sxp_files()
    through = k.select_file_to_use(gg, "p1 - 1, p2 -2")
    _p1_p3 = k.select_file_to_use(gg, "p1 - 1, p2 -3")
    _p1_p4 = k.select_file_to_use(gg, "p1 - 1, p2 - 4")
    _p2_p3 = k.select_file_to_use(gg, "p1 - 2, p2 - 3")
    _p2_p4 = k.select_file_to_use(gg, "p1 - 2, p2 - 4")
    ls_files: list[str] = [through, _p1_p3, _p2_p3, _p1_p4, _p2_p4] 
    #k.plot_parameter(through, S_Parameter.S11)
    dc_files: dict[str, list[S_Parameter]] = {
        through: [S_Parameter.S12, S_Parameter.S21],
        _p1_p3: [S_Parameter.S21],
        _p1_p4: [S_Parameter.S21],
        _p2_p3: [S_Parameter.S21],
        _p2_p4: [S_Parameter.S21]
    }

    legend_texts: list[str] = [
        k.get_s_param_text_for_legend(S_Parameter.S12), 
        k.get_s_param_text_for_legend(S_Parameter.S21),
        k.get_s_param_text_for_legend(S_Parameter.S31),
        k.get_s_param_text_for_legend(S_Parameter.S41),
        k.get_s_param_text_for_legend(S_Parameter.S32),
        k.get_s_param_text_for_legend(S_Parameter.S42)
        ]

    k.plot_multiple_on_one_graph(params_per_file=dc_files, frequency_unit=Frequency_Unit.MHz)
    k.change_legend_text(legend_texts)
    k.set_plot_title("Directional coupler S parameters")
    k.show_plot()