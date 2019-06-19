# coding=utf-8
# @Time    : 2019/5/14 11:10
# @Author  : Mandy

import os
import sys
if __name__ == '__main__':
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    sys.path.append(file_path)
    # print(file_path)
    # print(sys.path)
    os.system("Python ./testcases/article.py")


