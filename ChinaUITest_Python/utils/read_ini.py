# coding=utf-8
import configparser
import os


class ReadIni:

    def __init__(self, file_path=None):

        if file_path == None:
            self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "/elements/android/all.ini"
        else:
            self.file_path = file_path
        # self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "/elements/android/all.ini"
        self.data = self.read_ini()

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

