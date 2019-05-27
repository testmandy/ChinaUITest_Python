# coding=utf-8

from Android_StudyChina.testcases.article import driver


class Swipe:
    # 获取屏幕的宽高
    def get_size(self):
        size = driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self):
        # 设想size的返回类型为[100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        driver.swipe(x1, y1, x, y1)

    # 向右滑动
    def swipe_right(self):
        # 设想size的返回类型为[100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        driver.swipe(x1, y1, x, y1)

    # 向上滑动
    def swipe_up(self):
        # 设想size的返回类型为[100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        driver.swipe(x1, y1, x1, y)

    # 向下滑动
    def swipe_down(self):
        # 设想size的返回类型为[100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
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