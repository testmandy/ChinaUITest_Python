# coding=utf-8
from appium import webdriver

from Android_TalkU.utils.server import Server

# '''
# 为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程
# 我们将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
# '''
#
#
# class SuperDriver(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(SuperDriver, cls).__new__(cls, *args, **kwargs)
#         return cls._instance


class BaseDriver:

    def get_driver(self):
        server = Server()
        device1 = server.get_devices()[0]
        print("已连接的第一个设备：" + device1)
        capabilities = {
            "platformName": "Android",
            "deviceName": device1,
            "app": "C:\\Users\\user\\Downloads\\TalkU.apk",
            # "appWaitActivity": "me.dingtone.app.im.activity.WelcomeActivity",
            "appWaitActivity": "me.talkyou.app.im.activity.TalkuMainActivity",
            "appPackage": "me.talkyou.app.im",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)

        return driver






