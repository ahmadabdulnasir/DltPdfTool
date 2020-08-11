#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shu'aib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2020, salafi'
__version__ = "0.01t"
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,)
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap, QIcon, QPalette, QBrush
from PyQt5.QtCore import QTimer, pyqtSlot, QSize
import os
from controllers import path_gen



class MainWindow(QMainWindow):
    ''' Qt window object that defines the window of faces tracking '''
    def __init__(self,  parent):
        super(MainWindow, self).__init__()
        loadUi(path_gen.mainUiFile, self) # Loading UI
        self.setWindowTitle("DLT PDF Manupluations Tool")
        
        self.dialogs = list() # To be able raise another window (dialog)
        # Setting Background image



def boot():
    app = QApplication([])
    main = MainWindow(None)
    main.setToolTip("DaboLinux Technologies PDF Manupluations Tool")
    main.setWindowIcon(QIcon(path_gen.iconImg))
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    boot()
