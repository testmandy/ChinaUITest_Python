# coding=utf-8
import os
import time

from ChinaUITest_Python.utils.get_by_local import GetByLocal
from ChinaUITest_Python.utils.server import Server
from ChinaUITest_Python.common.base_driver import BaseDriver


class Article:
    def __init__(self):
        # 实例化server
        self.server = Server()
        self.server.main()
        # 调用get_driver
        self.base_driver = BaseDriver()
        self.driver = self.base_driver.android_driver()
        print("开始运行APP")
        # 实例化GetByLocal
        self.starter = GetByLocal(self.driver)
        # swipe = Swipe(driver)

    def capture(self, name):
        # 截图
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '_' + name + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)

    def read(self):
        time.sleep(5)
        # 点击学习
        self.starter.get_element("study_tab", "Study")[2].click()
        time.sleep(3)
        # 点击第一篇文章
        self.starter.get_element("article", "Study")[0].click()
        # swipe.swipe_on("up")
        time.sleep(10)
        # 获取截屏
        self.capture("article")
        # 点击返回按钮
        self.starter.get_element("back_button", "Study")[0].click()
        time.sleep(3)
        # 点击第2篇文章
        self.starter.get_element("article", "Study")[1].click()
        time.sleep(10)
        # 点击返回按钮
        self.starter.get_element("back_button", "Study")[0].click()


if __name__ == '__main__':
    article = Article()
    article.read()


