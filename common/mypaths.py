# coding=utf-8
# @Time    : 2019/7/10 11:05
# @Author  : Mandy
import os


project_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(project_dir, 'log\\')

report_dir = os.path.join(project_dir, 'report\\')

elements_dir = os.path.join(project_dir, 'elements')

android_elements_dir = os.path.join(elements_dir, 'android\\elements.ini')
android_axis_dir = os.path.join(elements_dir, 'android\\axis.ini')

screenshots_dir = os.path.join(project_dir, 'screenshots\\')
screenshots_list = os.path.join(project_dir, 'screenshots')

config_dir = os.path.join(project_dir, 'config')

userconfig_dir = os.path.join(config_dir, 'userconfig.yaml')

