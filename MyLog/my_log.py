#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-27 18:30
# @Author  : jingxuyang
# @FileName: loguru_test.py


from loguru import logger
print(logger.add('file_{time:YYYY-MM-DD}.log',format=" [v1] [{time:YYYY-MM-DD HH:mm:ss.hhh}] [{level}] [{thread}] {file} [TID: N/A] {name} {message} ", level="INFO", rotation='1GB', encoding='utf-8'))
# print(logger.add('/chj/log_test/file_{time:YYYY-MM-DD}.log',format=" [v1] [{time:YYYY-MM-DD HH:mm:ss.hhh}] [{level}] [{thread}] {file} [TID: N/A] {name} {message} ", level="INFO", rotation='1GB', encoding='utf-8'))
# print(logger.add('file_{time}.log',format=" [v1] [{time:YYYY-MM-DD HH:mm:ss.hhh}] [{level}] [{thread}] {file} [TID: N/A] {name} {message} ", level="INFO", backtrace=True, diagnose=True, rotation='5MB', encoding='utf-8'))

# logger.debug("hey, beautiful and simple logging!")
logger.info('hey, beautiful and simple logging!')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')
# logger.success('success')

# @logger.catch()
# def my_function(x,y,z):
#     return 1/(x+y+z)
# my_function(0,0,0)

def func(a,b):
    return a/b
def nested(c):
    try:
        d = func(5,c)
        logger.info("result: {}", d)
    except Exception:
        logger.exception("What?")
# nested(3)