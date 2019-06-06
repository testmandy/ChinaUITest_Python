# coding=utf-8
# @Time    : 2019/5/31 10:12
# @Author  : Mandy
import os

import yaml


class WriteUserConfig:
    def __init__(self):
        try:
            self.file_path = '../config/userconfig.yaml'
        except Exception as msg:
            print(u"文件不存在%s" % msg)
        else:
            try:
                self.file_path = './config/userconfig.yaml'
            except Exception as msg:
                print(u"文件不存在%s" % msg)


    '''
    加载yaml数据
    '''
    def read_data(self):
        with open(self.file_path, 'r') as fr:
            data = yaml.load(fr, Loader=yaml.Loader)
        return data

    '''
    获取value值
    '''
    def get_value(self, key):
        data = self.read_data()
        value = data['device1'][key]
        return value

    '''
    写入yaml数据
    '''
    def write_data(self, device, bp, port):
        data = self.join_data(device, bp, port)
        with open(self.file_path, 'a') as fr:
            yaml.dump(data, fr)

    '''
    拼接数据
    '''
    def join_data(self, device, bp, port):
        data = {
            "device1":
                {"deviceName": device,
                 "bp": bp,
                 "port": port}
        }
        return data

    '''
    清除yaml数据
    '''
    def clear_data(self):
        try:
            with open(self.file_path, 'w') as fr:
                fr.truncate()
        except Exception as msg:
            print(u"文件不存在%s" % msg)
            os.system("pause")
        else:
            fr.close()



# if __name__ == '__main__':
#     write_file = WriteUserConfig()
#     write_file.write_data("1111111", "4000", "4200")
#     device1 = write_file.get_value('deviceName')
#     port = write_file.get_value('port')
#     print(device1)
#     print(port)
#     write_file.clear_data()
