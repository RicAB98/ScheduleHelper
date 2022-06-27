from PyQt6.QtWidgets import *
from PyQt6 import uic
import PyQt6.QtCore
from Subject import Subject
from TableInformation import TableInformation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Designs/MainWindow.ui", self)

        self.numberSubjects = 0
        self.subjects = []

        self.ConnectButtons()

    def ConnectButtons(self):
        self.addClassButton.clicked.connect(self.AddClass)
        self.addSubjectButton.clicked.connect(self.AddSubject)

    def AddClass(self):
        name = self.classLineEdit.text()
        day = self.day.currentText()
        start = self.start.currentText()
        end = self.end.currentText()

        self.scheduleList.addItem(f'{day} - {start} - {end} ({name})')

    def AddSubject(self):
        classes = []

        for x in range(self.scheduleList.count()): #Get classes from List Widget
            classes.append(self.scheduleList.item(x).text())

        subject = Subject(self.subjectLineEdit.text(), classes) #Create new Subject object
        subject.comboBox.currentIndexChanged.connect(lambda: self.SubjectComboBoxChanged(subject))


        self.subjectsLayout.itemAt(self.numberSubjects).addWidget(subject) #Get first available Layout slot to put subject
        self.subjects.append(subject) #Append to subject to Window property
        self.numberSubjects += 1

        self.UpdateTable(subject, 0)
        self.ClearAddSubjectInputs()

    #Add new subject to table
    def UpdateTable(self, subject, index):
        if subject.classCells:
            self.ClearSubjectFromTable(subject)

        firstSchedule = subject.classes[index]
        
        column = TableInformation.GetColumnFromText(firstSchedule.day)
        startRow = TableInformation.GetRowFromText(firstSchedule.start)
        finalRow = TableInformation.GetRowFromText(firstSchedule.end)

        for row in range(startRow, finalRow): #Insert subject on every row from start to finish
            item = QTableWidgetItem(subject.name)
            item.setTextAlignment(0x0084) #Align center vertically and horizontaly
            
            self.schedule.setItem(row, column, item)
            subject.AddClassCell(row, column)

    def ClearSubjectFromTable(self, subject):
        for cell in subject.classCells:
            print(self.schedule.item(0,0))
            self.schedule.setItem(cell["row"], cell["column"], None)

        subject.classCells.clear()
  
    def ClearAddSubjectInputs(self):
        self.scheduleList.clear()
        self.classLineEdit.clear()
        self.subjectLineEdit.clear()

    def SubjectComboBoxChanged(self, subject):
        index = subject.comboBox.currentIndex()

        self.UpdateTable(subject, index)