# coding=utf-8
import os
import time

from ChinaUITest_Python.common.base_driver import BaseDriver
from ChinaUITest_Python.utils.get_by_local import GetByLocal

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

class ShowAds:

    def message_list(self):
        time.sleep(3)
        # 点击Contacts后再切换到Messages，用来获取广告
        starter.get_element("Contact_tab", "Contact").click()
        time.sleep(3)
        # 点击More
        starter.get_element("More_tab", "More").click()
        time.sleep(3)
        # 点击Messages
        starter.get_element("Messages_tab", "Messages").click()
        time.sleep(3)
        # 点击More
        starter.get_element("More_tab", "More").click()
        time.sleep(3)
        # 点击Messages
        starter.get_element("Messages_tab", "Messages").click()
        time.sleep(3)
        # 获取截屏
        capture("Message_list")

    def team(self):
        time.sleep(3)
        # 点击小秘书TalkU Team
        starter.get_element("TalkU_Team", "Messages")[2].click()
        time.sleep(3)
        # 获取截屏
        capture("Team")
        # 返回上一页
        starter.get_element("chat_back_button", "Messages").click()
        time.sleep(3)
        # 获取截屏
        capture("Message_list2")

    def us_sms(self):
        time.sleep(3)
        # 点击写短信
        starter.get_element("write_button", "Messages").click()
        time.sleep(3)
        # 点击第一个美国号码
        starter.get_element("number_list", "Messages")[1].click()
        time.sleep(3)
        # 获取截屏
        capture("SMS")
        # 返回上一页
        starter.get_element("chat_back_button", "Messages").click()

    def connect(self):
        time.sleep(3)
        # 点击Connect
        starter.get_element("Connect_tab", "Connect").click()
        time.sleep(3)
        # 获取截屏
        capture("Connect")

    def lottery(self):
        time.sleep(3)
        # 点击Lottery
        starter.get_element("lottery", "Connect").click()
        time.sleep(3)
        # 获取截屏
        capture("Lottery")

    def redeem(self):
        time.sleep(3)
        # 点击More
        starter.get_element("More_tab", "More").click()
        time.sleep(3)
        # 点击Redeem
        starter.get_element("Redeem", "More").click()
        time.sleep(3)
        # 获取截屏
        capture("Redeem")
        # 返回上一页
        starter.get_element("redeem_back_button", "More").click()

    def get_credits(self):
        time.sleep(3)
        # 点击Get Free Credits
        starter.get_element("GetMoreCredits", "More").click()
        time.sleep(3)
        # 点击Check-in
        starter.get_element("Checkin", "More").click()
        time.sleep(3)
        # 点击Check in Now
        starter.get_element("CheckinNow", "More").click()
        time.sleep(2)
        # 获取截屏
        capture("GetCredits")
        time.sleep(8)
        # 获取截屏
        capture("GetCredits2")
        # 点击关闭小黑屏幕
        starter.get_element("FN_ad_close", "More")
        # # 点击关闭全屏广告
        # driver.find_element_by_class_name("android.widget.ImageButton")
        time.sleep(3)
        # 获取截屏
        capture("GetCredits3")
        # 返回上一页
        starter.get_element("checkin_back_button", "More").click()


if __name__ == '__main__':
    showAds = ShowAds()
    showAds.message_list()
    showAds.team()
    showAds.us_sms()
    showAds.connect()
    showAds.redeem()
    showAds.get_credits()



