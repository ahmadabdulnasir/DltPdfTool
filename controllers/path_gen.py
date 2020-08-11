#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shu'aib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2020, salafi'
__version__ = "0.01t"
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Base directory were the current file is
PROJECT_ROOT = os.path.dirname(BASE_DIR)

ICONS_DIR = os.path.join(PROJECT_ROOT, 'assets')
UIS_DIR = os.path.join(PROJECT_ROOT, 'ui')

iconImg = os.path.join(ICONS_DIR, 'icon.png')
errorImg = iconImg
bgImg = os.path.join(BASE_DIR, 'main_window_bg.jpg')

mainUiFile = os.path.join(UIS_DIR, 'mainWindow.ui')
confFile = os.path.join(UIS_DIR, 'configurations.conf')



def boot():
    pass

if __name__ == "__main__":
    boot()
