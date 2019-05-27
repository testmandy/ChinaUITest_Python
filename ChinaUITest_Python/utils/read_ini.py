# coding=utf-8
import configparser


class ReadIni:

    def __init__(self):
        self.file_path = "D:/work/PycharmProjects/AppiumPython/Android_StudyChina/elements/android/all.ini"
        self.data = self.read_ini()

        # if file_path == None:
        #     self.file_path = "E:/PycharmProjects/AppiumPython/Android_TalkU/elements/android/all.ini"
        # else:
        #     self.file_path = file_path

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self, key, section=None):
        if section == None:
            section = 'More'
        else:
            section = section
        return self.data.get(section, key)

