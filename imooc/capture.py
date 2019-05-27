# coding=utf-8
import os
import time
from Android_TalkU.common.base_driver import BaseDriver

# 实例化driver
base_driver = BaseDriver()
# 调用get_driver
driver = base_driver.get_driver()


class Capture:
    def capture(self, name):
        # 截图
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + time2 + '_' + name + '.png'
        driver.get_screenshot_as_file(screen_save_path)


# 实例化Capture
capture = Capture()


