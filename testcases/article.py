# coding=utf-8
import time

import pytest

from common.base_driver import BaseDriver
from utils.server import Server
from utils.operation import Operation


def setup_module():
    global operation, driver
    # 调用get_driver
    server = Server()
    server.main()
    base_driver = BaseDriver(0)
    driver = base_driver.android_driver()
    # 实例化Operation
    operation = Operation(driver)
    print('[MyLog]--------OPERATION is inited NOW')


def teardown_module():
    print(u'[MyLog]--------关闭driver')
    driver.quit()


class TestArticle(object):
    def teardown_function(self):
        """每个测试用例执行之后做操作"""
        print(u'[MyLog]--------用例执行后')
        flag = operation.find_element("study_tab", "Study")
        print(flag)
        while flag is False:
            operation.tap_test("back_button")
            flag = operation.find_element("study_tab", "Study")
        print(u'[MyLog]--------用例执行完成，开始执行下一个')

    def setup_function(self):
        """每个测试用例执行之前做操作"""
        print(u'[MyLog]--------用例执行前')

    # @pytest.mark.skip
    def test_read(self):
        """
        测试用例：阅读文章
        """
        print('[MyLog]--------Begin running [test_read]')
        time.sleep(15)
        page = operation.get_element("page", "Study")
        tabs = operation.get_son_element(page, "articles", "Study")
        # 轮询点击【tab】
        for j in range(2, 15):
            try:
                print(u"[MyLog]--------点击第" + str(j) + "个tab")
                tabs[j].click()
                # # 向上滑动
                # operation.swipe_on("up")
                time.sleep(2)
                # 轮询点击每一篇文章
                print(u"[MyLog]--------获取文章列表")
                articles = operation.get_element("articles", "Study")
                for i in range(0, 1):
                    print(u"[MyLog]--------点击第" + str(i) + "篇文章")
                    articles[i].click()
                    # 上下滑动
                    print("[MyLog]--------开始上滑")
                    operation.swipe_on("up")
                    # operation.swipe_on("down")
                    # 添加收藏
                    print("[MyLog]--------开始添加收藏")
                    operation.tap_test("add_favorite")
                    # 点击分享
                    print("[MyLog]--------点击分享")
                    operation.tap_test("share")
                    operation.waiting_click(1, "share_methods", "Contacts", 0)
                    # 点击第一个最近联系人
                    operation.waiting_click(2, "friends", "Contacts", 0)
                    # 点击确认发送按钮
                    operation.waiting_click(1, "confirm", "Common")
                    # '''
                    # 点击添加评论
                    print("[MyLog]--------点击评论")
                    operation.tap_test("add_views")
                    operation.waiting_send_keys(1, "add_comment", "Study", "坚持走中国特色社会主义道路")
                    # 点击发布评论
                    print("[MyLog]--------发布评论")
                    operation.waiting_click(2, "add_comment_button", "Study", 1)
                    # 删除评论
                    print("[MyLog]--------点击删除评论")
                    views_frame = operation.get_element("views_frame", "Study")
                    text = operation.get_son_element(views_frame, "text", "Study")
                    text[7].click()
                    # 点击确认删除按钮
                    print("[MyLog]--------确认删除")
                    operation.waiting_click(2, "confirm", "Common")
                    time.sleep(30)
                    print("[MyLog]--------获取截屏")
                    operation.capture("read_" + str(i))
                    # 点击返回按钮
                    print("[MyLog]--------返回上一页")
                    operation.tap_test("back_button")
                time.sleep(2)
            except Exception as msg:
                print(u"[MyLog]--------查找元素异常%s" % msg)
            else:
                time.sleep(1)

    # @pytest.mark.skip
    def test_watch_video(self):
        """
        测试用例：视听学习
        """
        # 点击视听学习
        operation.waiting_click(5, "home_bottom_tab_icon", "Common", 2)
        # 点击【联播视频】
        page = operation.get_element("page", "Video")
        videos = operation.get_son_element(page, "videos", "Video")
        videos[4].click()
        # 点击第一个【新闻联播】
        videos[9].click()
        time.sleep(1000)
        # 点击返回按钮
        operation.tap_test("back_button")
        # 轮询点击【tab】

        for j in range(2, 5):
            try:
                videos[j].click()
                # 向上滑动
                operation.swipe_on("up")
                time.sleep(2)
                # 轮询点击每一个视频
                for i in range(10, 17, 2):
                    try:
                        videos[i].click()
                    except Exception as msg:
                        print(u"[MyLog]--------查找元素异常%s" % msg)
                    else:
                        time.sleep(15)
                        # 获取截屏
                        operation.capture("watch_video_" + str(i))
                        # 点击返回按钮
                        operation.tap_test("back_button")
                    continue
                time.sleep(3)
            except Exception as msg:
                print(u"[MyLog]--------查找元素异常%s" % msg)
            else:
                time.sleep(1)

        for k in range(8, 18):
            try:
                videos[k].click()
                # 向上滑动
                operation.swipe_on("up")
                time.sleep(2)
                # 轮询点击每一个视频
                for i in range(10, 17, 2):
                    try:
                        videos[i].click()
                    except Exception as msg:
                        print(u"[MyLog]--------查找元素异常%s" % msg)
                    else:
                        time.sleep(15)
                        # 获取截屏
                        operation.capture("watch_video_" + str(i))
                        # 点击返回按钮
                        operation.tap_test("back_button")
                    continue
                time.sleep(3)
            except Exception as msg:
                print(u"[MyLog]--------查找元素异常%s" % msg)
            else:
                time.sleep(1)

