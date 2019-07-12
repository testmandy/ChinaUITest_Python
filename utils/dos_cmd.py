# coding=utf-8
import os


class DosCmd:
    def excute_cmd_result(self, command):
        """
        执行cmd命令，并返回result
        :param command:需要执行的命令语句
        :return:result_list
        """
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == "\n":
                continue
            result_list.append(i.strip("\n"))
        return result_list

    def excute_cmd(self, command):
        """
        执行cmd命令，无返回值
        :param command:需要执行的命令语句
        :param command:需要执行的命令语句
        """
        os.system(command)

