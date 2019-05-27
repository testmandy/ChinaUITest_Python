# coding=utf-8
# @Time    : 2019/5/14 12:47
# @Author  : Mandy
from Android_StudyChina.utils.dos_cmd import DosCmd

class Port:
    def __init__(self):
        self.dos = DosCmd()

    def port_is_used(self, port_num):
        flag = None
        result = self.dos.excute_cmd_result("netstat -aon|findstr " + str(port_num))
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, devices_list):
        '''
        生成可用端口
        :param start_port: 起始端口号，如4700
        :param devices_list: 已连接设备数量
        :return:
        '''
        port_list = []
        if devices_list !=None:
            while len(port_list) != len(devices_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port = start_port + 1
            print(port_list)
            return port_list
        else:
            print("生成可用端口失败")
            return None


if __name__ == '__main__':
    port = Port()
    port.port_is_used("4000")
    port.create_port_list(4000, [1, 2, 3])
    # port.create_appium_command()
