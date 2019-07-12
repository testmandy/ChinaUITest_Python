# coding=utf-8
import time
import unittest
from common.base_driver import BaseDriver
from utils.server import Server
from utils.operation import Operation


class Article(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        global operation, driver
        # 调用get_driver
        server = Server()
        server.main()
        base_driver = BaseDriver(0)
        driver = base_driver.android_driver()
        # 实例化Operation
        operation = Operation(driver)

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print(u'关闭driver')
        driver.quit()

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print(u'用例执行后')
        flag = operation.find_element("study_tab", "Study")
        print(flag)
        while flag is False:
            operation.tap_test("back_button")
            flag = operation.find_element("study_tab", "Study")
        print(u'用例执行完成，开始执行下一个')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(u'用例执行前')

    def test_read(self):
        """
        测试用例：阅读文章
        """
        time.sleep(5)
        # 点击学习
        operation.waiting_click(2, "study_tab", "Study")
        # 点击【要闻】
        page = operation.get_element("page", "Study")
        tabs = operation.get_son_element(page, "articles", "Study")
        # tabs[3].click()
        # 轮询点击【tab】
        for j in range(2, 10):
            try:
                tabs[j].click()
                # 向上滑动
                operation.swipe_on("up")
                time.sleep(2)
                # 轮询点击每一篇文章
                articles = operation.get_element("articles", "Study")
                for i in range(0, 3):
                    try:
                        articles[i].click()
                    except Exception as msg:
                        print(u"查找元素异常%s" % msg)
                    else:
                        # 上下滑动
                        operation.swipe_on("up")
                        operation.swipe_on("down")
                        # 添加收藏
                        operation.tap_test("add_favorite")
                        # 点击分享
                        operation.tap_test("share")
                        operation.waiting_click(1, "share_methods", "Contacts", 0)
                        # 点击第一个最近联系人
                        operation.waiting_click(2, "friends", "Contacts", 0)
                        # 点击确认发送按钮
                        operation.waiting_click(1, "confirm", "Common")
                        # '''
                        # 点击添加评论
                        operation.tap_test("add_views")
                        operation.waiting_send_keys(1, "add_comment", "Study", "坚持走中国特色社会主义道路")
                        # 点击发布评论
                        operation.waiting_click(2, "add_comment_button", "Study", 1)
                        # 删除评论
                        views_frame = operation.get_element("views_frame", "Study")
                        text = operation.get_son_element(views_frame, "text", "Study")
                        text[7].click()
                        # 点击确认删除按钮
                        operation.waiting_click(2, "confirm", "Common")
                        time.sleep(15)
                        # 获取截屏
                        operation.capture("read_" + str(i))
                        # 点击返回按钮
                        operation.tap_test("back_button")
                    continue
                time.sleep(2)
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(1)

    def test_watch_video(self):
        """
        测试用例：视听学习
        """
        # 点击视听学习
        operation.waiting_click(2, "video_tab", "Video")
        # 点击【联播视频】
        page = operation.get_element("page", "Video")
        videos = operation.get_son_element(page, "videos", "Video")
        videos[4].click()
        # 点击第一个【新闻联播】
        videos[9].click()
        time.sleep(10)
        # 点击返回按钮
        operation.tap_test("back_button")

        # 轮询点击【tab】
        for j in range(2, 9):
            try:
                videos[j].click()
                # # 向上滑动
                # operation.swipe_on("up")
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
                        operation.capture("watch_video_" + str(i))
                        # 点击返回按钮
                        operation.tap_test("back_button")
                    continue
                time.sleep(3)
            except Exception as msg:
                print(u"查找元素异常%s" % msg)
            else:
                time.sleep(1)

