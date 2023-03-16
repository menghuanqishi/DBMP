# ！/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 author : 梦幻骑士
 email  : wp_226@163.com
 @Project : DBMP
 @File  : setting.PY
 @Time  : 2023/3/16 10:11
 @Desc  :
"""
from os import path as os_path
from sys import path as sys_path

BASE_DIR = os_path.dirname(os_path.dirname(__file__))
sys_path.append(BASE_DIR)
# 配置文件路径
CONFIG_FILE = os_path.join(BASE_DIR, "config", "config.ini")
# 基础库目录
LIBS_DIR = os_path.join(BASE_DIR, "libs")
# 控制类目录
cONTROLLER_LOG = os_path.join(BASE_DIR, "controller")
# 模块类目录
MODEL_FILE = os_path.join(BASE_DIR, "model")
# 显示类目录
VIEW_FILE = os_path.join(BASE_DIR, "model")
# 日志目录
LOG_DIR = os_path.join(BASE_DIR, "logs")
# 程序版本
VERSION = 'V1.0.0.0'
# 变更日期
MODIFY_DATE = '2023-3-16'