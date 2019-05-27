# coding=utf-8

import logging

from Android_TalkU.utils.dos_cmd import DosCmd
from Android_TalkU.utils.port import Port


class Server:
    def get_devices(self):
        '''
        获取设备信息
        :return:设备列表devices_list
        '''
        dos = DosCmd()
        devices_list = []
        result_list = dos.excute_cmd_result("adb devices")
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split("\t")
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            logging.info('没有连接的设备')

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
        devices_list = self.get_devices()
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


if __name__ == '__main__':
    server = Server()
    server.create_appium_command()
