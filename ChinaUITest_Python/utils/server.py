# coding=utf-8

import time

from ChinaUITest_Python.utils.dos_cmd import DosCmd
from ChinaUITest_Python.utils.port import Port

import logging

# 创建Logger
from ChinaUITest_Python.utils.write_userconfig import WriteUserConfig

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Server:
    def __init__(self):
        self.dos = DosCmd()
        global port, bp, device1
        port = 4723
        bp = 4700
        device1 = self.get_devices()[0]
        self.write_file = WriteUserConfig()

    def get_devices(self):
        '''
        获取设备信息
        :return:设备列表devices_list
        '''
        devices_list = []
        # self.dos.excute_cmd_result("adb")
        time.sleep(2)
        try:
            result_list = self.dos.excute_cmd_result("adb devices")
        except Exception as msg:
            print(u"启动adb异常%s" % msg)
        time.sleep(2)
        print("----------------执行adb devices的结果长度为：" + str(len(result_list)) + "----------------")
        print(type(result_list))
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

    # def create_port_list(self, start_port, devices_list):
    #     '''
    #     生成可用端口
    #     :param start_port: 起始端口号，如4700
    #     :param devices_list: 已连接设备数量
    #     :return:
    #     '''
    #
    #     return port_list

    def create_appium_command(self):
        '''
        appium -p 4723 -bp 4701 -U 159beaa8
        :return:command_list
        '''
        port = Port()
        command_list = []
        time.sleep(2)
        devices_list = self.get_devices()
        time.sleep(2)
        print(devices_list)
        port.create_port_list(4000, [1, 2, 3])
        print(port.create_port_list(4700, ['1', '2']))

        appium_port_list = port.create_port_list(4700, devices_list)
        print(appium_port_list)

        bootstrap_port_list = port.create_port_list(4900, devices_list)
        print(bootstrap_port_list)

        for i in range(len(devices_list)):
            command = "appium -p" + str(appium_port_list)[i] +" -bp " + str(bootstrap_port_list)[i] \
                      + "-U" + devices_list[i] + "-no -reset"
            command_list.append(command)

        print(command_list)
        return command_list

    def create_one_appium_command(self):
        '''
        appium -p 4723 -bp 4701 -U 159beaa8
        :return:appium_command
        os.system会阻塞进程，为避免不影响执行下一步，在命令前面一定要加start
        改为用os.system("start appium -a 127.0.0.1 -p %s -U %s")
        '''
        time.sleep(2)
        # devices_list = self.get_devices()
        time.sleep(2)
        print("启动appium前获取到设备为：" + str(device1))
        appium_command = "start appium -p " + str(port) + " -bp " + str(bp) + " -U " + device1 + " --no-reset"
        logger.info("现在启动Appium服务")
        print("现在启动Appium服务:" + appium_command)
        self.write_file.write_data(device1, bp, port)
        return appium_command

    def start_server(self):
        self.start_appium = self.create_one_appium_command()
        self.dos.excute_cmd(self.start_appium)

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self):
        self.kill_server()
        self.write_file.clear_data()
        self.start_server()
        time.sleep(2)



