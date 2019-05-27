# coding=utf-8
import os
result_list = []


class DosCmd:
    def excute_cmd_result(self, command):
        result = os.popen(command).readlines()
        for i in result:
            if i == "\n":
                continue
            result_list.append(i.strip("\n"))
        return result_list


