from PyQt6.QtWidgets import *
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Designs/MainWindow.ui", self)