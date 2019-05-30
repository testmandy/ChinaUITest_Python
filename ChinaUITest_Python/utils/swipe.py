# coding=utf-8
# from ChinaUITest_Python.testcases.login import driver
#
#
# class Swipe(driver):
#     # 获取屏幕的宽高
#     def get_size(self):
#         size = driver.get_window_size()
#         width = size['width']
#         height = size['height']
#         return width, height
#
#     # 向左滑动
#     def swipe_left(self):
#         # 设想size的返回类型为[100,200]
#         x1 = self.get_size()[0] / 10 * 9
#         y1 = self.get_size()[1] / 2
#         x = self.get_size()[0] / 10
#         driver.swipe(x1, y1, x, y1)
#
#     # 向右滑动
#     def swipe_right(self):
#         # 设想size的返回类型为[100,200]
#         x1 = self.get_size()[0] / 10
#         y1 = self.get_size()[1] / 2
#         x = self.get_size()[0] / 10 * 9
#         driver.swipe(x1, y1, x, y1)
#
#     # 向上滑动
#     def swipe_up(self):
#         # 设想size的返回类型为[100,200]
#         x1 = self.get_size()[0] / 2
#         y1 = self.get_size()[1] / 10 * 9
#         y = self.get_size()[1] / 10
#         driver.swipe(x1, y1, x1, y)
#
#     # 向下滑动
#     def swipe_down(self):
#         # 设想size的返回类型为[100,200]
#         x1 = self.get_size()[0] / 2
#         y1 = self.get_size()[1] / 10
#         y = self.get_size()[1] / 10 * 9
#         driver.swipe(x1, y1, x1, y)
#
#     # 不同方向
#     def swipe_on(self, direction):
#         if direction == "left":
#             self.swipe_left()
#         elif direction == "right":
#             self.swipe_right()
#         elif direction == "up":
#             self.swipe_up()
#         else:
#             self.swipe_down()
#
#     def taptest(self):
#         # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
#         a1 = 42 / 720
#         b1 = 88 / 1280
#         # 获取当前手机屏幕大小X,Y
#         x0 = self.get_size()[0]
#         y0 = self.get_size()[1]
#         # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
#         driver.tap([(a1 * x0, b1 * y0)])
