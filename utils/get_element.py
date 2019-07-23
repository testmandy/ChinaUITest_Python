# coding=utf-8
import conftest
from utils.read_ini import ReadIni


class GetElement:

    def get_axis(self, key):
        """
        获取坐标轴数据，并返回value
        :param key: ini文件中的key
        :return:x, y轴的值
        """
        file_path = conftest.android_axis_dir
        read_ini = ReadIni(file_path)
        axis = read_ini.get_value(key)
        if axis is not None:
            x = axis.split(",")[0]
            y = axis.split(",")[1]
            return x, y
        else:
            return None

    def get_element(self, driver, key, section):
        """
        查找页面元素
        :param driver: 设备驱动
        :param key: ini文件中的key
        :param section: ini文件中的section
        :return:查找结果element
        """
        read_ini = ReadIni()
        local = read_ini.get_value(key, section)
        if local is not None:
            by = local.split(">")[0]
            location = local.split(">")[1]
            if by == "id":
                try:
                    return driver.find_element_by_id(location)
                except Exception as msg:
                    print(u"查找元素异常%s" % msg)
                    return None
            elif by == "ids":
                try:
                    return driver.find_elements_by_id(location)
                except Exception as msg:
                    print(u"查找元素异常%s" % msg)
            elif by == "className":
                try:
                    return driver.find_element_by_class_name(location)
                except Exception as msg:
                    print(u"查找元素异常%s" % msg)
            elif by == "classNames":
                try:
                    return driver.find_elements_by_class_name(location)
                except Exception as msg:
                    print(u"查找元素异常%s" % msg)
            elif by == "text":
                try:
                    return driver.find_element_by_link_text(location)
                except Exception as msg:
                    print(u"查找元素异常%s" % msg)
            else:
                try:
                    return driver.find_element_by_xpath(location)
                except Exception as msg:
                    print(u"查找元素异常%s" % msg)
        else:
            return None
