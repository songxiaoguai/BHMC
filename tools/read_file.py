import os

import yaml

from tools.path_file import path_absolute


class ReadFiles:
    def read_txt(self, file_name):
        txt_data = []
        with open(path_absolute() + os.sep + "data" + file_name + ".txt", "r", encoding="utf-8") as f:
            for i in f:
                txt_data.append(i.strip().split(","))
        return txt_data

    def read_yaml(self,filename):
        with open(path_absolute() + os.sep + "data" + os.sep + filename, "r", encoding="utf-8") as f:
            return [tuple(i.values()) for i in yaml.safe_load(f).values()]


if __name__ == '__main__':
    read = ReadFiles()
    print(read.read_yaml("login.yaml"))