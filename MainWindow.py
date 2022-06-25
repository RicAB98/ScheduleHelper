from PyQt6.QtWidgets import *
from PyQt6 import uic
from Subject import Subject

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Designs/MainWindow.ui", self)

        self.numberSubjects = 0

        self.ConnectButtons()

    def ConnectButtons(self):
        self.addClassButton.clicked.connect(self.AddClass)
        self.addSubjectButton.clicked.connect(self.AddSubjectButton)

    def AddClass(self):
        day = self.day.currentText()
        start = self.start.currentText()
        end = self.end.currentText()

        self.scheduleList.addItem(f'{day} - {start} - {end}')

    def AddSubjectButton(self):
        subject = Subject(self.subjectLineEdit.text())
        print(self.subjectsLayout.count())

        self.subjectsLayout.itemAt(self.numberSubjects).addWidget(subject)
        self.numberSubjects += 1
        print("Adding subject")