# coding=utf-8
import os
import time

from Android_StudyChina.utils.get_by_local import GetByLocal
from Android_StudyChina.common.base_driver import BaseDriver

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

class Login:

    def __init__(self, telephone, password):
        self.telephone = telephone
        self.password = password

    def go_login(self):
        time.sleep(3)
        # 点击-Already have account?
        starter.get_element("have_account_button", "Enter").click()

    def login(self):
        time.sleep(2)
        # 输入手机号
        starter.get_element("telephone", "Login").send_keys(self.telephone)
        # 点击Continue进入下一步
        starter.get_element("continue_button", "Login").click()
        time.sleep(2)
        # 输入密码
        starter.get_element("password", "Login").send_keys(self.password)
        # 点击Login登录
        starter.get_element("login_button", "Login").click()
        time.sleep(2)
        # 出现弹窗，点击确认
        starter.get_element("continue_alert", "Common").click()
        time.sleep(2)

    def logout(self):
        # 点击More
        starter.get_element("More_tab", "More").click()
        time.sleep(2)
        # 点击Settings
        starter.get_element("Settings", "More").click()
        time.sleep(2)
        # 点击Account Settings
        starter.get_element("Account_Settings", "More").click()
        time.sleep(2)
        # 点击My Devices on TalkU
        starter.get_element("My_Devices", "More").click()
        time.sleep(2)
        # 点击注销按钮
        starter.get_element("deactivate_button", "More").click()
        time.sleep(10)
        # 出现弹窗，点击确认注销
        starter.get_element("continue_alert", "Common").click()
        time.sleep(2)
        # 出现弹窗，再次点击确认
        starter.get_element("continue2_alert", "Common").click()
        capture()


def capture():
    # 截图
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    time2 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time2 + '.png'
    driver.get_screenshot_as_file(screen_save_path)


if __name__ == '__main__':
    test = Login("3159782580", "123456")
    test.go_login()
    test.login()
    # test.logout()



