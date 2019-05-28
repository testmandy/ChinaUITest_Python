# coding=utf-8
import time

from appium import webdriver

from ChinaUITest_Python.utils.server import Server


# '''
# 为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程
# 我们将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
# '''


class SuperDriver(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SuperDriver, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class BaseDriver(SuperDriver):
    def android_driver(self):
        server = Server()
        device1 = server.get_devices()[0]
        port = server.port
        print("已连接的第一个设备：" + device1)
        capabilities = {
            "platformName": "Android",
            "deviceName": device1,
            "app": "E:\\360Downloads\\cn.xuexi.android_508.apk",
            "appWaitActivity": "com.alibaba.android.rimet.biz.SplashActivity",
            "appPackage": "cn.xuexi.android",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + str(port) + "/wd/hub", capabilities)
        time.sleep(5)
        return driver







