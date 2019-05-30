# coding=utf-8
from ChinaUITest_Python.utils.read_ini import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, session):
        readIni = ReadIni()
        local = readIni.get_value(key, session)
        if local != None:
            by = local.split(">")[0]
            location = local.split(">")[1]
            if by == "id":
                return self.driver.find_element_by_id(location)
            elif by == "ids":
                return self.driver.find_elements_by_id(location)
            elif by == "className":
                return self.driver.find_element_by_class_name(location)
            elif by == "classNames":
                return self.driver.find_elements_by_class_name(location)
            elif by == "text":
                return self.driver.find_element_by_link_text(location)
            else:
                return self.driver.find_element_by_xpath(location)
        else:
            return None

