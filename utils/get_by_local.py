# coding=utf-8
from utils.read_ini import ReadIni


class GetByLocal:
    def __init__(self):
        self.readIni = ReadIni()

    def get_element(self, driver, key, section):
        """
        查找页面元素
        :param driver: 设备驱动
        :param key: ini文件中的key
        :param section: ini文件中的section
        :return:查找结果element
        """
        read_ini = self.readIni
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

