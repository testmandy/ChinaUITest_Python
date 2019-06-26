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
        time.sleep(5)
        # 点击学习
        self.starter.get_element("study_tab", "Study").click()
        time.sleep(1)
        # 点击【要闻】
        page = self.starter.get_element("page", "Study")
        tabs = self.starter.get_elements_element(page, "articles", "Study")
        # tabs[3].click()
        # 轮询点击【tab】
        for j in range(3, 10):
            try:
                tabs[j].click()
                # 向上滑动
                self.swipe.swipe_on("up")
                time.sleep(2)
                # 轮询点击每一篇文章
                articles = self.starter.get_element("articles", "Study")
                for i in range(0, 3):
                    try:
                        articles[i].click()
                    except Exception as msg:
                        print(u"查找元素异常%s" % msg)
                    else:
                        time.sleep(1)
                        # 向上滑动
                        self.swipe.swipe_on("up")
                        time.sleep(1)
                        self.swipe.swipe_on("down")
                        time.sleep(1)
                        # 添加收藏
                        self.swipe.tap_test("add_favorite")
                        time.sleep(1)
                        # 点击分享
                        self.swipe.tap_test("share")
                        time.sleep(2)
                        self.starter.get_element("share_methods", "Contacts")[0].click()
                        time.sleep(2)
                        # 点击第一个最近联系人
                        self.starter.get_element("friends", "Contacts")[0].click()
                        time.sleep(1)
                        # 点击确认发送按钮
                        self.starter.get_element("confirm", "Common").click()
                        time.sleep(10)
                        # 点击添加评论
                        self.swipe.tap_test("add_views")
                        self.starter.get_element("add_comment", "Study").send_keys("坚持走中国特色社会主义道路")
                        # 点击发布评论
                        self.starter.get_element("add_comment_button", "Study")[1].click()
                        time.sleep(2)
                        # 删除评论
                        views_frame = self.starter.get_element("views_frame", "Study")
                        text = self.starter.get_elements_element(views_frame, "text", "Study")
                        text[7].click()
                        # 点击确认删除按钮
                        self.starter.get_element("confirm", "Common").click()
                        time.sleep(2)
                        # 获取截屏
                        self.swipe.capture("read_" + str(i))
                        # 点击返回按钮
                        self.swipe.tap_test("back_button")
                    continue
                time.sleep(2)
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(1)

    def watch_video(self):
        time.sleep(3)
        # 点击视听学习
        self.starter.get_element("video_tab", "Video").click()
        time.sleep(3)
        # 点击【联播视频】
        page = self.starter.get_element("page", "Video")
        videos = self.starter.get_elements_element(page, "videos", "Video")
        videos[4].click()
        # 点击第一个【新闻联播】
        videos[9].click()
        time.sleep(1080)
        # 点击返回按钮
        self.swipe.tap_test("back_button")

        # 轮询点击【tab】
        for j in range(2, 9):
            try:
                videos[j].click()
                # # 向上滑动
                # self.swipe.swipe_on("up")
                time.sleep(2)
                # 轮询点击每一个视频
                for i in range(10, 17, 2):
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

            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(1)


if __name__ == '__main__':
    article = Article()
    article.read()
    article.watch_video()


