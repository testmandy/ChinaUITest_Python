# coding=utf-8

from appium import webdriver


def get_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "159beaa8",
        "app": "C:\\Users\\user\\Downloads\\imooc7.apk",
        "appPackage": "cn.com.open.mooc",
        # "appWaitActivity": "com.imooc.component.imoocmain.splash.GuideActivity",
        "appWaitActivity": "com.imooc.component.imoocmain.index.MCMainActivity",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver


# 获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height


# 向左滑动
def swipe_left():
    # 设想size的返回类型为[100,200]
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1)


# 向右滑动
def swipe_right():
    # 设想size的返回类型为[100,200]
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1)


# 向上滑动
def swipe_up():
    # 设想size的返回类型为[100,200]
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y)


# 向下滑动
def swipe_down():
    # 设想size的返回类型为[100,200]
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


# 不同方向
def swipe_on(direction):
    if direction == "left":
        swipe_left()
    elif direction == "right":
        swipe_right()
    elif direction == "up":
        swipe_up()
    else:
        swipe_down()


driver = get_driver()
# swipe_on("left")
# time.sleep(1)
# swipe_on("left")
# swipe_on("left")
# swipe_on("left")


def go_login():
    elements = driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
    elements[3].click()
    driver.find_element_by_id("cn.com.open.mooc:id/header_line").click()
    # driver.find_element_by_id("cn.com.open.mooc:id/right_text").click()


def login():
    driver.find_element_by_id("cn.com.open.mooc:id/accountEdit").send_keys("15558038582")
    driver.find_element_by_id("cn.com.open.mooc:id/passwordEdit").send_keys("123456")
    driver.find_element_by_id("cn.com.open.mooc:id/login").click()


go_login()
login()


