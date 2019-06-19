# coding=utf-8
import time
import os
from common.base_driver import BaseDriver
from utils.get_by_local import GetByLocal
from utils.server import Server
from utils.get_by_axis import GetByAxis


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
        time.sleep(3)
        # 点击学习
        self.starter.get_element("study_tab", "Study").click()
        time.sleep(2)
        # 轮询点击每一篇文章
        articles = self.starter.get_element("article", "Study")
        for i in range(0, 3):
            try:
                articles[i].click()
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(5)
                # 添加收藏
                self.taptest("add_favorite")
                time.sleep(3)
                # 点击添加评论
                self.taptest("add_views")
                self.starter.get_element("add_comment", "Study").send_keys(u"坚持走中国特色社会主义道路")
                # 点击发布评论
                self.starter.get_element("add_comment_button", "Study")[1].click()
                time.sleep(5)
                # 获取截屏
                self.capture("read_" + str(i))
                # 点击返回按钮
                self.taptest("back_button")
            continue
        time.sleep(2)

    def watch_video(self):
        time.sleep(3)
        # 点击视听学习
        self.starter.get_element("video_tab", "Video").click()
        time.sleep(3)
        # 点击第三个tab联播频道
        # try:
        #     son_tabs = self.starter.get_element("son_tabs", "Video")
        # except InvalidSelectorException as msg:
        #     print(u"查找方法无效%s" % msg)
        # else:
        #     son_tabs[3].click()
        # 点击第1个视频
        # self.taptest("video_one")
        # # self.starter.get_element("article", "Study")[0].click()
        # time.sleep(60)
        # # 获取截屏
        # self.capture("watch_video")
        # # 点击返回按钮
        # self.taptest("back_button")
        # time.sleep(3)
        # 轮询点击每一个视频
        videos = self.starter.get_element("videos", "Video")
        for i in range(6, 9):
            try:
                videos[i].click()
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(10)
                # 获取截屏
                self.capture("watch_video_" + str(i))
                # 点击返回按钮
                self.taptest("back_button")
            continue
        time.sleep(3)


if __name__ == '__main__':
    article = Article()
    article.read()
    article.watch_video()


