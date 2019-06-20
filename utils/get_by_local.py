# coding=utf-8
from utils.read_ini import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver
        self.readIni = ReadIni()

    def get_element(self, key, section):
        local = self.readIni.get_value(key, section)
        if local is not None:
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

    def get_elements_element(self, elements, key, section):
        local = self.readIni.get_value(key, section)
        if local is not None:
            by = local.split(">")[0]
            location = local.split(">")[1]
            if by == "id":
                return elements.find_element_by_id(location)
            elif by == "ids":
                return elements.find_elements_by_id(location)
            elif by == "className":
                return elements.find_element_by_class_name(location)
            elif by == "classNames":
                return elements.find_elements_by_class_name(location)
            elif by == "text":
                return elements.find_element_by_link_text(location)
            else:
                return elements.find_element_by_xpath(location)
        else:
            return None
