from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
from MainWindow import MainWindow
from Subject import Subject

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    s = Subject("LCOM", ["14:00-14:30 - 2ª", "16:00-16:30 - 2ª","14:00-14:30 - 6ª","18:00-18:30 - 6ª"])
    a = Subject("LCOM", ["14:00-14:30 - 2ª"])
    b = Subject("LCOM", ["14:00-14:30 - 2ª"])
    c = Subject("LCOM", ["14:00-14:30 - 2ª"])
    d = Subject("LCOM", ["14:00-14:30 - 2ª"])
    e = Subject("LCOM", ["14:00-14:30 - 2ª"])
    window.subjectsLayout.itemAt(0).addWidget(s)
    window.subjectsLayout.itemAt(1).addWidget(a)
    window.subjectsLayout.itemAt(2).addWidget(b)
    window.subjectsLayout.itemAt(3).addWidget(c)
    window.subjectsLayout.itemAt(4).addWidget(d)
    window.subjectsLayout.itemAt(5).addWidget(e)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()