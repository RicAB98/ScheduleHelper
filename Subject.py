import sched
from tkinter.font import names
from PyQt6.QtWidgets import *
from PyQt6 import uic
from Class import Class

class Subject(QWidget):
    def __init__(self, name, classes = None):
        super().__init__()
        uic.loadUi("Designs/SubjectLayout.ui", self)

        self.name = name
        self.classes = []
        self.classCells = []

        self.label.setText(name + ": ")
        
        if classes is not None:
            for c in classes:
                self.classes.append(Class(c))

            self.comboBox.addItems(classes)

    def AddClassCell(self, row, column):
        self.classCells.append({"row": row, "column": column})
