# coding=utf-8
import configparser
import os


class ReadIni:

    def __init__(self, file_path=None):
        """
        初始化元素的文件地址
        :param file_path: ini文件地址
        """
        if file_path is None:
            self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + \
                             "/config/android/elements.ini"
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        """
        读取文件
        """
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding="utf-8")
        return read_ini

    def get_value(self, key, section=None):
        """
        获取文件中key对应的value值
        :param key: ini文件中的key
        :param section: ini文件中的section，默认为空
        """
        if section is None:
            section = 'Axis'
        else:
            section = section
        return self.data.get(section, key)


