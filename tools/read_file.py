import os

from bhmc.tools.path_file import path_absolute


class ReadFiles():
    def read_txt(self, file_name):
        txt_data = []
        with open(path_absolute() + os.sep + "data" + file_name + ".txt", "r", encoding="utf-8") as f:
            for i in f:
                txt_data.append(i.strip().split(","))
        return txt_data
