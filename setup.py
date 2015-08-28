#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Control_DB_date',
    version='2.0.0',
    author='rfyiamcool',
    author_email='rfyiamcool@163.com',
    packages=find_packages(),
    url='https://github.com/rfyiamcool',
    description='get dbname from date and dbname , According to the monthly',
    long_description=open('README.md').read(),
    install_requires=['IPy==0.81'],
    license='MIT'
)
