# coding=utf-8
import os

from ChinaUITest_Python.utils.read_ini import ReadIni


class GetByAxis:
    def __init__(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "/config/android/axis.ini"

    def get_axis(self, key):
        readIni = ReadIni(self.file_path)
        axis = readIni.get_value(key)
        if axis != None:
            x = axis.split(",")[0]
            y = axis.split(",")[1]
            return x, y
        else:
            return None


# if __name__ == '__main__':
#     getbyaxis = GetByAxis()
#     local = getbyaxis.get_axis("back_button")
#     print(local[0])


