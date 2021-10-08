#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-10-08 10:30
# @Author  : jingxuyang
# @FileName: setup.py
from setuptools import setup, find_packages

setup(
    # 包名
    name = "MyLog",
    #  版本
    version = "0.1",
    # git地址
    url = "https://github.com/jingxuyangcoco/python_sdk_demo.git",
    # 包的解释地址
    long_description = open('ReadMe.md', encoding='utf-8').read(),
    # 需要包含的子包列表
    packages = find_packages()
)