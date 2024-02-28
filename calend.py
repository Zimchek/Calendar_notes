import calendar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from datetime import datetime
from PyQt5.QtCore import QDate
import os
import time
from random import randint


# TODO Сделать кнопку для очистки всех заметок в папке Заметки. Но только предварительно переспросить "Точно хотите удалить все заметки из папки?"
# TODO При запуске программы делать автоматически файл с текущей датой и временем в папке "Журнал"


class Ui_MainWindow(QMainWindow):
    if not os.path.exists("Заметки"):
        os.mkdir("Заметки")
    os.chdir("Заметки")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(534, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        # self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        # self.calendarWidget.setObjectName("calendarWidget")
        # self.gridLayout.addWidget(self.calendarWidget, 1, 2, 3, 1)

        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        # self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendar = QCalendarWidget(self.centralwidget)
        self.calendar.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendar, 1, 2, 3, 1)

        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.printDateInfo)

        # место ввода
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 2)
        # кнопка открывания
        self.open = QPushButton("Открыть")
        self.gridLayout.addWidget(self.open, 3, 0, 1, 1)
        self.open.clicked.connect(self.openFile)
        # кнопка сохранения
        self.save = QPushButton("Сохранить")
        self.gridLayout.addWidget(self.save, 3, 1, 1, 1)
        self.save.clicked.connect(self.saveFile)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.calendar.clicked.connect(self.plainTextEdit.clear)

    # вывод в консоль выбранную дату
    def printDateInfo(self, qDate):
        global year_note, month_note, day_note
        print("{0}/{1}/{2}".format(qDate.month(), qDate.day(), qDate.year()))
        month_note = format(qDate.month())
        day_note = format(qDate.day())
        year_note = format(qDate.year())
        print(year_note, month_note, day_note)

    # функции кнопок
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Календарь"))
        self.label.setText(_translate("MainWindow", "Календарные заметки"))
        self.label_2.setText(_translate("MainWindow", "Описание события:"))

    # функция сохранения файла
    def saveFile(self, qDate):
        salt_ = randint(1, 999)
        file_name = f"{year_note}-{month_note}-{day_note}---{salt_}.txt"
        if not os.path.exists(file_name):
            fname = QFileDialog.getSaveFileName(self, "Save File", file_name)[0]
            text = self.plainTextEdit.toPlainText()
            with open(fname + ".txt", "w") as f:
                f.write(text)

    # функция открывания файла
    def openFile(self):
        fname = QFileDialog.getOpenFileName(
            self, "Open File", ".", "Text Files (.txt);;All Files ()"
        )[0]
        if fname:
            with open(fname, "r") as file:
                data = file.read()
                self.plainTextEdit.setPlainText(data)

    # def openFile(self):
    #   filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (.txt);;All Files ()")
    #  if filename:
    #      with open(filename, 'r') as file:
    #         contents = file.read()
    #     print(contents)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
