# coding=utf-8
import os
import time

from Android_StudyChina.common.base_driver import BaseDriver
from Android_StudyChina.utils.get_by_local import GetByLocal

# 实例化driver
base_driver = BaseDriver()
# 调用get_driver
driver = base_driver.get_driver()
# 实例化GetByLocal
starter = GetByLocal(driver)

def capture(name):
    # 截图
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time2 + '_' + name + '.png'
    driver.get_screenshot_as_file(screen_save_path)


class Article:
    def read(self):
        time.sleep(3)
        # 点击强国通
        starter.get_element("qiang_tab", "Qiang")[0].click()
        time.sleep(3)
        # 点击第一篇文章
        starter.get_element("article", "Qiang")[0].click()
        time.sleep(10)
        # 获取截屏
        capture("article")
        # 点击返回按钮
        starter.get_element("back_button", "Qiang")[0].click()
        time.sleep(3)
        # 点击第2篇文章
        starter.get_element("article", "Qiang")[1].click()
        time.sleep(10)
        # 点击返回按钮
        starter.get_element("back_button", "Qiang")[0].click()



if __name__ == '__main__':
    article = Article()
    article.read()

