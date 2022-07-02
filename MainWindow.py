from PyQt6.QtWidgets import *
from PyQt6 import uic
import PyQt6.QtGui as QtGui
from JSONHelper import JsonHelper
from Subject import Subject
from TableInformation import TableInformation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Designs/MainWindow.ui", self)

        self.numberSubjects = 0
        self.subjects = []
        self.conflicts = {}

        self.SetSignals()

    def SetSignals(self):
        self.addClassButton.clicked.connect(self.AddClass)
        self.addSubjectButton.clicked.connect(self.AddSubject)
        self.scheduleList.itemDoubleClicked.connect(self.RemoveItem)
        self.exportButton.clicked.connect(self.ExportToJson)

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

        subject = Subject(self.numberSubjects, self.subjectLineEdit.text(), classes) #Create new Subject object
        subject.comboBox.currentIndexChanged.connect(lambda: self.SubjectComboBoxChanged(subject))
        subject.removeButton.clicked.connect(lambda: self.RemoveSubject(subject))

        self.subjectsLayout.itemAt(self.numberSubjects).addWidget(subject) #Get first available Layout slot to put subject
        self.numberSubjects += 1

        self.UpdateTable(subject, 0)
        self.ClearAddSubjectInputs()

    def RemoveItem(self, item):
        row = self.scheduleList.row(item)
        self.scheduleList.takeItem(row)

    def ExportToJson(self):
        subjects = []

        for n in range(self.numberSubjects):
            subject = self.subjectsLayout.itemAt(n).itemAt(0).widget()
            subjects.append(subject)

        JsonHelper.ConvertTo(subjects)

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

            cellContent = self.schedule.item(row, column)

            if cellContent is not None:
                self.AddConflictBackground(item)
                self.SetConflict(row, column, subject.name, cellContent.text())

            self.schedule.setItem(row, column, item)
            subject.AddClassCell(row, column)

    def ClearSubjectFromTable(self, subject):
        for cell in subject.classCells:
            item = None

            conflict = self.conflicts.get(f'{cell["row"]},{cell["column"]}')

            if conflict is not None:
                conflict.remove(subject.name)
                item = QTableWidgetItem(conflict[0])
                item.setTextAlignment(0x0084) #Align center vertically and horizontaly

                if len(conflict) == 1:
                    del self.conflicts[f'{cell["row"]},{cell["column"]}']
                else:
                    self.AddConflictBackground(item)

            self.schedule.setItem(cell["row"], cell["column"], item)

        subject.classCells.clear()
  
    def ClearAddSubjectInputs(self):
        self.scheduleList.clear()
        self.classLineEdit.clear()
        self.subjectLineEdit.clear()

    def AddConflictBackground(self, item):
        color = QtGui.QBrush(QtGui.QColor(255, 100, 100))   
        item.setBackground(color)

    def SetConflict(self, row, column, newSubject, existingSubject):
        if f'{row},{column}' in self.conflicts:
            self.conflicts[f'{row},{column}'].append(newSubject)
        else:
            self.conflicts[f'{row},{column}'] = [existingSubject, newSubject]

    def SubjectComboBoxChanged(self, subject):
        index = subject.comboBox.currentIndex()

        self.UpdateTable(subject, index)

    def RemoveSubject(self, subject):
        layoutId = subject.layoutId

        #Remove subject from Layout
        self.ClearSubjectFromTable(subject)
        subject.setParent(None)
        del subject

        for n in range(layoutId + 1, self.numberSubjects): #Push below subject up one layout
            topLayout = self.subjectsLayout.itemAt(n - 1)
            bottomLayout = self.subjectsLayout.itemAt(n)
            widget = bottomLayout.itemAt(0).widget()

            widget.layoutId -= 1
            topLayout.addWidget(widget)
            print(widget.name)

        print("\n\n\n")

        self.numberSubjects -= 1