import sched
from PyQt6.QtWidgets import *
from PyQt6 import uic

class Subject(QWidget):
    def __init__(self, name, schedules = None):
        super().__init__()
        uic.loadUi("Designs/SubjectLayout.ui", self)
        self.label.setText(name + ": ")
        if schedules is not None:
            self.comboBox.addItems(schedules)