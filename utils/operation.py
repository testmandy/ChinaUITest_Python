# coding=utf-8
import os
import time

from utils.get_element import GetElement


class Operation:
    def __init__(self, driver):
        self.driver = driver
        print("[MyLog]--------Start to run testcase")
        # 获取当前手机屏幕大小X,Y
        self.width = self.get_size()[0]
        self.height = self.get_size()[1]
        # 实例化GetElement
        self.starter = GetElement()

    def capture(self, name):
        """
        定义截图方法
        :param name: 图片命名
        """
        time.sleep(2)
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '_' + name + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)

    def get_element(self, key, section):
        """
        获取页面元素
        :param key: ini文件中的key
        :param section: ini文件中的section
        :return:element
        """
        return self.starter.get_element(self.driver, key, section)

    def get_son_element(self, father_element, key, section):
        """
        获取父元素下的子元素
        :param father_element: 父元素
        :param key: ini文件中的key
        :param section: ini文件中的section
        :return:element
        """
        return self.starter.get_element(father_element, key, section)

    def waiting_click(self, timeout, key, section, i=None):
        """
        封装方法，等待几秒后再点击操作
        :param timeout: 等待时间
        :param key: ini文件中的key
        :param section: ini文件中的section
        :param i:第i个元素
        """
        time.sleep(timeout)
        if i is None:
            self.starter.get_element(self.driver, key, section).click()
        else:
            self.starter.get_element(self.driver, key, section)[i].click()

    def waiting_send_keys(self, timeout, key, section, message, i=None):
        """
        封装方法，等待几秒后再输入字符串
        :param timeout: 等待时间
        :param key: ini文件中的key
        :param section: ini文件中的section
        :param message: 需要输入的字符串
        :param i:第i个元素
        """
        time.sleep(timeout)
        if i is None:
            self.starter.get_element(self.driver, key, section).send_keys(message)
        else:
            self.starter.get_element(self.driver, key, section)[i].send_keys(message)

    def find_element(self, key, section):
        """
        查看（判断）页面是否有某元素
        :param key: ini文件中的key
        :param section: ini文件中的section
        :return:True or False
        """
        time.sleep(1)
        element_info = str(self.starter.get_element(self.driver, key, section))
        print(element_info)
        if 'element' in element_info:
            flag = True
        else:
            flag = False
        return flag

    def get_size(self):
        """
        获取屏幕大小
        :return:屏幕的宽高 width, height
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self):
        """
        向左滑动
        设想size的返回类型为[100,200]
        """
        # 设想size的返回类型为[100,200]
        x1 = self.width / 10 * 9
        y1 = self.height / 2
        x = self.width / 10
        self.driver.swipe(x1, y1, x, y1)

    def swipe_right(self):
        """
        向右滑动
        设想size的返回类型为[100,200]
        """
        x1 = self.width / 10
        y1 = self.height / 2
        x = self.width / 10 * 9
        self.driver.swipe(x1, y1, x, y1)

    def swipe_up(self):
        """
        向上滑动
        设想size的返回类型为[100,200]
        """
        x1 = self.width / 2
        y1 = self.height / 10 * 9
        y = self.height / 10
        self.driver.swipe(x1, y1, x1, y)

    def swipe_down(self):
        """
        向下滑动
        设想size的返回类型为[100,200]
        """
        x1 = self.width / 2
        y1 = self.height / 10
        y = self.height / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def swipe_on(self, direction):
        """
        传入方向值，实现一个方法在不同方向滑动
        :param direction: 方向值
        """
        time.sleep(1)
        if direction == "left":
            self.swipe_left()
        elif direction == "right":
            self.swipe_right()
        elif direction == "up":
            self.swipe_up()
        else:
            self.swipe_down()

    def tap_test(self, key):
        """
        根据屏幕定位点击元素
        :param key: ini文件中的key
        :param waiting_time: 等待时间
        """
        time.sleep(2)
        # 设定系数，控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        x = int(self.starter.get_axis(key)[0])
        y = int(self.starter.get_axis(key)[1])
        x1 = x / 720
        y1 = y / 1280
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver.tap([(x1 * self.width, y1 * self.height)])
