# coding=utf-8
import time
from appium import webdriver

# '''
# 为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程
# 我们将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
# '''
from utils.write_userconfig import WriteUserConfig


# class SuperDriver(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(SuperDriver, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

class BaseDriver:
    def __init__(self, i):
        write_file = WriteUserConfig()
        self.device = write_file.get_value('device' + str(i), 'deviceName')
        self.port = write_file.get_value('device' + str(i), 'port')

    def android_driver(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": self.device,
            # 可以通过newcommandtimeout将超时时间改长，超时时间可按照实际情况自定义
            "newCommandTimeout": "2000",
            "app": "E:\\360Downloads\\cn.xuexi.android_508.apk",
            "appWaitActivity": "com.alibaba.android.rimet.biz.SplashActivity",
            "appPackage": "cn.xuexi.android",
            "noReset": "true",
            "unicodeKeyboard": "true",  # 使用Unicode编码方式发送字符串
            "resetKeyboard": "true"  # 隐藏键盘
        }
        try:
            driver = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capabilities)
        except Exception as msg:
            print(u"connection error：%s" % msg)
            time.sleep(1)
            driver2 = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capabilities)
            return driver2
        else:
            time.sleep(1)
            return driver

    def iOS_driver(self):
        # 配置信息
        print("iOS driver已连接的第一个设备：" + self.device)
        capabilities = {
            "platformName": "iOS",
            "deviceName": "iPhone 6s",
            # 可以通过newcommandtimeout将超时时间改长，超时时间可按照实际情况自定义
            "newCommandTimeout": "2000",
            "udid": "601861ce25a7dae4dc3d12e6f43cd42936XXXXXX",
            "automationName": "XCUITest",
            "xcodeOrgId": "7GTPKLXXXX",
            "xcodeSigningId": "iPhone Developer",
            "no-reset": "true",
            "startIWDP": "true",
            "bundleId": "com.XXXXXX"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + str(self.port) + "/wd/hub", capabilities)
        time.sleep(5)
        return driver










