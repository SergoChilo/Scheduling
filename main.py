import json
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView
from PyQt5.uic import loadUi

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main_page.ui", self)


app = QApplication(sys.argv)
main = main_window()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
