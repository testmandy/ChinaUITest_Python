# coding=utf-8
import time
import sys
import os
from appium import webdriver
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# '''
# 为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程
# 我们将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
# '''
from utils.write_userconfig import WriteUserConfig


class SuperDriver(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SuperDriver, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class BaseDriver(SuperDriver):
    def __init__(self):
        write_file = WriteUserConfig()
        self.device1 = write_file.get_value('deviceName')
        self.port = write_file.get_value('port')

    def android_driver(self):
        print("Android driver已连接的第一个设备：" + self.device1)
        capabilities = {
            "platformName": "Android",
            "deviceName": self.device1,
            # 可以通过newcommandtimeout将超时时间改长，超时时间可按照实际情况自定义
            "newCommandTimeout": "2000",
            "app": "E:\\360Downloads\\cn.xuexi.android_508.apk",
            "appWaitActivity": "com.alibaba.android.rimet.biz.SplashActivity",
            "appPackage": "cn.xuexi.android",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capabilities)
        time.sleep(3)
        return driver







