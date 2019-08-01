# coding=utf-8
# @Time    : 2019/5/14 11:10
# @Author  : Mandy

import os
import conftest

if __name__ == '__main__':
    os.system("pytest -v " + conftest.case_dir)

