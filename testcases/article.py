# coding=utf-8
import time
from common.base_driver import BaseDriver
from utils.get_by_local import GetByLocal
from utils.server import Server
from utils.swipe import Swipe


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
        self.swipe = Swipe(self.driver)

    def read(self):
        time.sleep(2)
        # 点击学习
        self.starter.get_element("study_tab", "Study").click()
        time.sleep(1)
        # 点击【要闻】
        page = self.starter.get_element("page", "Study")
        self.starter.get_elements_element(page, "articles", "Study")[3].click()
        # 轮询点击每一篇文章
        articles = self.starter.get_element("articles", "Study")
        for i in range(0, 4):
            try:
                articles[i].click()
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(1)
                # 向上滑动
                self.swipe.swipe_on("up")
                time.sleep(5)
                self.swipe.swipe_on("down")
                time.sleep(5)
                # 添加收藏
                self.swipe.tap_test("add_favorite")
                time.sleep(1)
                '''
                # 点击添加评论
                self.swipe.tap_test("add_views")
                self.starter.get_element("add_comment", "Study").send_keys("坚持走中国特色社会主义道路")
                # 点击发布评论
                self.starter.get_element("add_comment_button", "Study")[1].click()
                time.sleep(5)
                '''
                # 获取截屏
                self.swipe.capture("read_" + str(i))
                # 点击返回按钮
                self.swipe.tap_test("back_button")
            continue
        time.sleep(2)

    def watch_video(self):
        time.sleep(3)
        # 点击视听学习
        self.starter.get_element("video_tab", "Video").click()
        time.sleep(3)
        # 点击【联播视频】
        page = self.starter.get_element("page", "Video")
        self.starter.get_elements_element(page, "videos", "Video")[4].click()
        # 点击第一个【新闻联播】
        self.starter.get_elements_element(page, "videos", "Video")[9].click()
        time.sleep(10)
        # 点击返回按钮
        self.swipe.tap_test("back_button")
        # 轮询点击每一个视频
        videos = self.starter.get_element("videos", "Video")
        for i in range(0, 5):
            try:
                videos[i].click()
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(15)
                # 获取截屏
                self.swipe.capture("watch_video_" + str(i))
                # 点击返回按钮
                self.swipe.tap_test("back_button")
            continue
        time.sleep(3)


if __name__ == '__main__':
    article = Article()
    article.read()
    article.watch_video()


