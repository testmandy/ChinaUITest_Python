# coding=utf-8
import os
import threading
import time
import logging

from utils.dos_cmd import DosCmd
from utils.write_userconfig import WriteUserConfig

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Server:
    def __init__(self):
        self.dos = DosCmd()
        global bp, port, device1
        bp = 4700
        port = 4723
        self.device_list = self.get_devices()
        device1 = self.device_list[0]
        self.write_file = WriteUserConfig()
        self.log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "\\log"

    def get_devices(self):
        """
        获取设备信息
        :return:设备列表devices_list
        """
        devices_list = []
        time.sleep(2)
        try:
            result_list = self.dos.excute_cmd_result("adb devices")
        except Exception as msg:
            print(u"启动adb异常%s" % msg)
        time.sleep(2)
        print("----------------执行adb devices的结果长度为：" + str(len(result_list)) + "----------------")
        print("执行adb devices的结果为：" + str(result_list))
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split("\t")
                time.sleep(2)
                try:
                    if devices_info[-1] == 'device':
                        devices_list.append(devices_info[0])
                except Exception as msg:
                    print(u"获取device失败%s" % msg)
                else:
                    time.sleep(2)
            return devices_list
        else:
            logger.info('没有连接的设备')

    def port_is_used(self, port_num):
        """
        判断端口是否被占用
        :param port_num: 检查的端口号
        :return:布尔值flag
        """
        command = "netstat -ano | findstr " + str(port_num)
        result = self.dos.excute_cmd_result(command)
        # print('检查端口是否被占用的结果' + str(result))
        # print(len(result))
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        生成可用端口
        :param start_port: 起始端口号，如4700
        :param devices_list: 已连接设备数量
        :return:
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print(u"生成可用端口失败")
            return None

    def create_appium_command(self, i):
        """
        appium -p 4723 -bp 4701 -U 159beaa8
        :param i: 第i个设备
        :return:command_list
        os.system会阻塞进程，为避免不影响执行下一步，在命令前面一定要加start
        改为用os.system("start appium -a 127.0.0.1 -p %s -U %s")
        """
        command_list = []
        time.sleep(2)
        print(self.device_list)
        appium_port_list = self.create_port_list(4700, self.device_list)
        bootstrap_port_list = self.create_port_list(4900, self.device_list)
        command = "start /b appium -p " + str((appium_port_list)[i]) + " -bp " + str((bootstrap_port_list)[i]) + " -U " + \
                  self.device_list[i] + " --no-reset --session-override --log " + self.log_path
        command_list.append(command)
        self.write_file.write_data(i, self.device_list[i], str((bootstrap_port_list)[i]), str((appium_port_list)[i]))
        return command_list

    def start_server(self, i):
        """
        定义方法：启动appium server
        :param i: 第i个设备
        """
        print("Starting server NOW")
        self.start_appium_list = self.create_appium_command(i)
        print(self.start_appium_list)
        self.dos.excute_cmd(self.start_appium_list[0])

    def kill_server(self):
        """
        定义方法：每次执行前先kill掉node进程
        """
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self):
        """
        多线程，执行main方法
        step1：kill server
        step2：clear file(userconfig.yaml)
        step3：根据生成的 appium list 分线程执行 start server
        """
        thread_list = []
        self.kill_server()
        self.write_file.clear_data()
        print("start write data to file: userconfig.yaml")
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(25)
