# coding=utf-8
import os
import time

from ChinaUITest_Python.utils.get_by_local import GetByLocal
from ChinaUITest_Python.utils.server import Server
from ChinaUITest_Python.common.base_driver import BaseDriver
from ChinaUITest_Python.utils.get_by_axis import GetByAxis



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
        self.getbyaxis = GetByAxis()


    def capture(self, name):
        # 截图
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '_' + name + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)

    def taptest(self, key):
        # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        x = int(self.getbyaxis.get_axis(key)[0])
        y = int(self.getbyaxis.get_axis(key)[1])
        a1 = x / 720
        b1 = y / 1280
        # 获取当前手机屏幕大小X,Y
        x0 = self.driver.get_window_size()['width']
        y0 = self.driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver.tap([(a1 * x0, b1 * y0)])


    def read(self):
        time.sleep(5)
        # 点击学习
        self.starter.get_element("study_tab", "Study").click()
        time.sleep(3)
        # 点击第一篇文章
        self.starter.get_element("article", "Study")[1].click()
        # swipe.swipe_on("up")
        time.sleep(10)
        # 获取截屏
        self.capture("read")
        # 点击返回按钮
        self.taptest("back_button")
        time.sleep(3)
        # 点击第2篇文章
        self.starter.get_element("article", "Study")[2].click()
        time.sleep(10)
        self.capture("article")
        # 点击返回按钮
        self.taptest("back_button")
        time.sleep(3)

    def watch_video(self):
        time.sleep(5)
        # 点击视听学习
        self.starter.get_element("video_tab", "Video").click()
        time.sleep(3)
        # 点击第三个tab联播频道
        self.starter.get_element("lianbo", "Video").click()
        # 点击第1个视频
        self.taptest("video_one")
        # self.starter.get_element("article", "Study")[0].click()
        time.sleep(60)
        # 获取截屏
        self.capture("watch_video")
        # 点击返回按钮
        self.taptest("back_button")
        time.sleep(3)
        # 点击第2个视频
        # self.starter.get_element("article", "Study")[1].click()
        # time.sleep(600)
        # self.capture("watch_video2")
        # 点击返回按钮
        # self.taptest("back_button")
        # time.sleep(3)


if __name__ == '__main__':
    article = Article()
    article.read()
    article.watch_video()


