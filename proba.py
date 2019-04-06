from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
import json
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 565)
        MainWindow.setMinimumSize(QtCore.QSize(440, 565))
        MainWindow.setMaximumSize(QtCore.QSize(440, 565))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLCDNumber(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(230, 10, 191, 41))
        self.display.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.display.setObjectName("display")
        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(230, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.num_2.setFont(font)
        self.num_2.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.num_2.setObjectName("num_2")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.num_2)
        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(300, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.num_1.setFont(font)
        self.num_1.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.num_1.setObjectName("num_1")
        self.buttonGroup.addButton(self.num_1)
        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        self.num_0.setGeometry(QtCore.QRect(370, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.num_0.setFont(font)
        self.num_0.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.num_0.setObjectName("num_0")
        self.buttonGroup.addButton(self.num_0)
        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setGeometry(QtCore.QRect(300, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.num_4.setFont(font)
        self.num_4.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.num_4.setObjectName("num_4")
        self.buttonGroup.addButton(self.num_4)
        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setGeometry(QtCore.QRect(370, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.num_3.setFont(font)
        self.num_3.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.num_3.setObjectName("num_3")
        self.buttonGroup.addButton(self.num_3)
        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setGeometry(QtCore.QRect(230, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.num_5.setFont(font)
        self.num_5.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.num_5.setObjectName("num_5")
        self.buttonGroup.addButton(self.num_5)
        self.save_weight = QtWidgets.QPushButton(self.centralwidget)
        self.save_weight.setGeometry(QtCore.QRect(20, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_weight.setFont(font)
        self.save_weight.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.save_weight.setObjectName("save_weight")
        self.add_button = QtWidgets.QRadioButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(240, 180, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QRadioButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(340, 180, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.save_marks = QtWidgets.QPushButton(self.centralwidget)
        self.save_marks.setGeometry(QtCore.QRect(230, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_marks.setFont(font)
        self.save_marks.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.save_marks.setObjectName("save_marks")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 300, 401, 161))
        self.textBrowser.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.textBrowser.setObjectName("textBrowser")
        self.spinBox_k = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_k.setGeometry(QtCore.QRect(90, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_k.setFont(font)
        self.spinBox_k.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.spinBox_k.setObjectName("spinBox_k")
        self.spinBox_f = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_f.setGeometry(QtCore.QRect(90, 120, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_f.setFont(font)
        self.spinBox_f.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.spinBox_f.setObjectName("spinBox_f")
        self.spinBox_t = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_t.setGeometry(QtCore.QRect(90, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_t.setFont(font)
        self.spinBox_t.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.spinBox_t.setObjectName("spinBox_t")
        self.pushButton_k = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_k.setGeometry(QtCore.QRect(20, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_k.setFont(font)
        self.pushButton_k.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.pushButton_k.setObjectName("pushButton_k")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.pushButton_k)
        self.pushButton_f = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_f.setGeometry(QtCore.QRect(20, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_f.setFont(font)
        self.pushButton_f.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.pushButton_f.setObjectName("pushButton_f")
        self.buttonGroup_2.addButton(self.pushButton_f)
        self.pushButton_t = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_t.setGeometry(QtCore.QRect(20, 180, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_t.setFont(font)
        self.pushButton_t.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.pushButton_t.setObjectName("pushButton_t")
        self.buttonGroup_2.addButton(self.pushButton_t)
        self.choose_subject = QtWidgets.QComboBox(self.centralwidget)
        self.choose_subject.setGeometry(QtCore.QRect(18, 11, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.choose_subject.setFont(font)
        self.choose_subject.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.choose_subject.setObjectName("choose_subject")
        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(20, 470, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_all.setFont(font)
        self.delete_all.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.delete_all.setObjectName("delete_all")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(230, 470, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settings.setFont(font)
        self.settings.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.settings.setObjectName("settings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор оценок"))
        self.num_2.setText(_translate("MainWindow", "2"))
        self.num_1.setText(_translate("MainWindow", "1"))
        self.num_0.setText(_translate("MainWindow", "0"))
        self.num_4.setText(_translate("MainWindow", "4"))
        self.num_3.setText(_translate("MainWindow", "3"))
        self.num_5.setText(_translate("MainWindow", "5"))
        self.save_weight.setText(_translate("MainWindow", "Сохранить вес"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.remove_button.setText(_translate("MainWindow", "Убрать"))
        self.save_marks.setText(_translate("MainWindow", "Сохранить оценки"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_k.setText(_translate("MainWindow", "К"))
        self.pushButton_f.setText(_translate("MainWindow", "Ф"))
        self.pushButton_t.setText(_translate("MainWindow", "Т"))
        self.delete_all.setText(_translate("MainWindow", "Сбросить все"))
        self.settings.setText(_translate("MainWindow", "Настройки"))



class Setting_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 565)
        MainWindow.setMinimumSize(QtCore.QSize(440, 565))
        MainWindow.setMaximumSize(QtCore.QSize(440, 565))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 70, 221, 51))
        self.comboBox.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.comboBox.setObjectName("comboBox")
        self.k5 = QtWidgets.QSpinBox(self.centralwidget)
        self.k5.setGeometry(QtCore.QRect(80, 220, 41, 41))
        self.k5.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.k5.setObjectName("k5")
        self.k4 = QtWidgets.QSpinBox(self.centralwidget)
        self.k4.setGeometry(QtCore.QRect(140, 220, 41, 41))
        self.k4.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.k4.setObjectName("k4")
        self.k3 = QtWidgets.QSpinBox(self.centralwidget)
        self.k3.setGeometry(QtCore.QRect(200, 220, 41, 41))
        self.k3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.k3.setObjectName("k3")
        self.k2 = QtWidgets.QSpinBox(self.centralwidget)
        self.k2.setGeometry(QtCore.QRect(260, 220, 41, 41))
        self.k2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.k2.setObjectName("k2")
        self.k1 = QtWidgets.QSpinBox(self.centralwidget)
        self.k1.setGeometry(QtCore.QRect(320, 220, 41, 41))
        self.k1.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.k1.setObjectName("k1")
        self.f1 = QtWidgets.QSpinBox(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(320, 280, 41, 41))
        self.f1.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.f1.setObjectName("f1")
        self.f3 = QtWidgets.QSpinBox(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(200, 280, 41, 41))
        self.f3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.f3.setObjectName("f3")
        self.f5 = QtWidgets.QSpinBox(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(80, 280, 41, 41))
        self.f5.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.f5.setObjectName("f5")
        self.f4 = QtWidgets.QSpinBox(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(140, 280, 41, 41))
        self.f4.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.f4.setObjectName("f4")
        self.f2 = QtWidgets.QSpinBox(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(260, 280, 41, 41))
        self.f2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.f2.setObjectName("f2")
        self.t1 = QtWidgets.QSpinBox(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(320, 340, 41, 41))
        self.t1.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.t1.setObjectName("t1")
        self.t3 = QtWidgets.QSpinBox(self.centralwidget)
        self.t3.setGeometry(QtCore.QRect(200, 340, 41, 41))
        self.t3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.t3.setObjectName("t3")
        self.t5 = QtWidgets.QSpinBox(self.centralwidget)
        self.t5.setGeometry(QtCore.QRect(80, 340, 41, 41))
        self.t5.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.t5.setObjectName("t5")
        self.t4 = QtWidgets.QSpinBox(self.centralwidget)
        self.t4.setGeometry(QtCore.QRect(140, 340, 41, 41))
        self.t4.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.t4.setObjectName("t4")
        self.t2 = QtWidgets.QSpinBox(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(260, 340, 41, 41))
        self.t2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.t2.setObjectName("t2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: white;\n"
"color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 340, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: white;\n"
"color: rgb(0, 170, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 160, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 160, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: white;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 160, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: white;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 160, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: white;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 160, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: white;")
        self.label_10.setObjectName("label_10")
        self.k0 = QtWidgets.QSpinBox(self.centralwidget)
        self.k0.setGeometry(QtCore.QRect(380, 220, 41, 41))
        self.k0.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.k0.setObjectName("k0")
        self.t0 = QtWidgets.QSpinBox(self.centralwidget)
        self.t0.setGeometry(QtCore.QRect(380, 340, 41, 41))
        self.t0.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.t0.setObjectName("t0")
        self.f0 = QtWidgets.QSpinBox(self.centralwidget)
        self.f0.setGeometry(QtCore.QRect(380, 280, 41, 41))
        self.f0.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.f0.setObjectName("f0")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 160, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: white;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 70, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: white;")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 420, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(240, 128, 128);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(20, 490, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.okButton.setObjectName("okButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Настройки"))
        self.label_3.setText(_translate("MainWindow", "К"))
        self.label_4.setText(_translate("MainWindow", "Ф"))
        self.label_5.setText(_translate("MainWindow", "Т"))
        self.label_6.setText(_translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "4"))
        self.label_8.setText(_translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Добавить"))
        self.label_13.setText(_translate("MainWindow", "Удалить"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить оценки"))
        self.okButton.setText(_translate("MainWindow", "Назад"))



class SettingWidget(QMainWindow, Setting_Window):
    def __init__(self, mark_dict, weight_dict):
        try:

            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.add)
            self.mark_dict = mark_dict
            self.weight_dict = weight_dict
            self.subjects = list(self.mark_dict.keys())
            # combobox
            self.comboBox.addItems(self.subjects)
            self.comboBox.activated[str].connect(self.onActivated)
            self.subject = None
            self.pushButton_2.clicked.connect(self.delete)
            self.pushButton_3.clicked.connect(self.save_marks)
            self.okButton.clicked.connect(self.main_window)
        except Exception as e:
            print('init', e)

    def add(self):
        try:
            name = self.lineEdit.text()
            if self.pushButton.sender() and bool(name):
                self.mark_dict[name] = {'new': {'k': [], 'f': [], 't': []},
                                        'saved': {'k': [], 'f': [], 't': []}}
                self.weight_dict[name] = [70, 20, 10]
                self.comboBox.addItem(name)
                self.subjects.append(name)
                self.onActivated(name)
        except Exception as e:
            print('add', e)

    def delete(self):
        try:
            if self.pushButton_2.sender() and self.subject:
                self.comboBox.removeItem(self.subjects.index(self.subject))
                self.subjects.remove(self.subject)
                del self.mark_dict[self.subject]
                del self.weight_dict[self.subject]
                self.subject = None
        except Exception as e:
            print('delete', e)

    def onActivated(self, text):
        try:
            self.subject = text
            self.k5.setValue(len([i for i in self.mark_dict[self.subject]['saved']['k'] if i == 5]))
            self.k4.setValue(len([i for i in self.mark_dict[self.subject]['saved']['k'] if i == 4]))
            self.k3.setValue(len([i for i in self.mark_dict[self.subject]['saved']['k'] if i == 3]))
            self.k2.setValue(len([i for i in self.mark_dict[self.subject]['saved']['k'] if i == 2]))
            self.k1.setValue(len([i for i in self.mark_dict[self.subject]['saved']['k'] if i == 1]))
            self.k0.setValue(len([i for i in self.mark_dict[self.subject]['saved']['k'] if i == 0]))
            self.f5.setValue(len([i for i in self.mark_dict[self.subject]['saved']['f'] if i == 5]))
            self.f4.setValue(len([i for i in self.mark_dict[self.subject]['saved']['f'] if i == 4]))
            self.f3.setValue(len([i for i in self.mark_dict[self.subject]['saved']['f'] if i == 3]))
            self.f2.setValue(len([i for i in self.mark_dict[self.subject]['saved']['f'] if i == 2]))
            self.f1.setValue(len([i for i in self.mark_dict[self.subject]['saved']['f'] if i == 1]))
            self.f0.setValue(len([i for i in self.mark_dict[self.subject]['saved']['f'] if i == 0]))
            self.t5.setValue(len([i for i in self.mark_dict[self.subject]['saved']['t'] if i == 5]))
            self.t4.setValue(len([i for i in self.mark_dict[self.subject]['saved']['t'] if i == 4]))
            self.t3.setValue(len([i for i in self.mark_dict[self.subject]['saved']['t'] if i == 3]))
            self.t2.setValue(len([i for i in self.mark_dict[self.subject]['saved']['t'] if i == 2]))
            self.t1.setValue(len([i for i in self.mark_dict[self.subject]['saved']['t'] if i == 1]))
            self.t0.setValue(len([i for i in self.mark_dict[self.subject]['saved']['t'] if i == 0]))
        except Exception as e:
            print('onActivated', e)

    def save_marks(self):
        try:
            if self.subject and self.pushButton_3.sender():
                self.mark_dict[self.subject]['saved']['k'] = [0] * self.k0.value() + [1] * self.k1.value() \
                                                             + [2] * self.k2.value() + [3] * self.k3.value() \
                                                             + [4] * self.k4.value() + [5] * self.k5.value()
                self.mark_dict[self.subject]['saved']['f'] = [0] * self.f0.value() + [1] * self.f1.value() \
                                                             + [2] * self.f2.value() + [3] * self.f3.value() \
                                                             + [4] * self.f4.value() + [5] * self.f5.value()
                self.mark_dict[self.subject]['saved']['t'] = [0] * self.t0.value() + [1] * self.t1.value() \
                                                             + [2] * self.t2.value() + [3] * self.t3.value() \
                                                             + [4] * self.t4.value() + [5] * self.t5.value()
        except Exception as e:
            print(e)

    def main_window(self):
        try:
            if self.okButton.sender():
                self.mw = MyWidget(self.mark_dict, self.weight_dict)
                self.mw.choose_subject.clear()
                self.mw.subjects = list(self.mw.mark_dict.keys())
                self.mw.choose_subject.addItems(self.subjects)
                self.auto = True
                self.mw.show()
                self.close()
        except Exception as e:
            print(e)

    def closeEvent(self, event, auto=False):
        try:
            if self.auto:
                event.accept()
            else:
                reply = QMessageBox.question(
                    self, 'Информация', "Вы уверены, что хотите выйти?",
                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    with open('weight.json', mode='w', encoding='utf-8') as file:
                        file.write(json.dumps(self.weight_dict))
                    with open('marks.json', mode='w', encoding='utf-8') as file:
                        file.write(json.dumps(self.mark_dict))
                    event.accept()
                else:
                    event.ignore()
        except Exception as e:
            print(e)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, mark_dict=False, weight_dict=False):
        try:
            super().__init__()
            self.setupUi(self)
            self.auto = False
            # Добавление словаря оценок
            if mark_dict:
                self.mark_dict = mark_dict
            else:
                try:
                    with open('marks.json', mode='r', encoding='utf-8') as file:
                        self.mark_dict = json.loads(file.read())
                except Exception as e:
                    self.mark_dict = {
                        'Алгебра': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Биология': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'География': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Геометрия': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Иностранный язык': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Информатика': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'История': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Литература': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Обществознание': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Русский язык': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Физика': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Физическая культура': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                        'Химия': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}}}
            if weight_dict:
                self.weight_dict = weight_dict
            else:
                # Добавление веса оценок
                try:
                    with open('weight.json', mode='r', encoding='utf-8') as file:
                        self.weight_dict = json.loads(file.read())
                except Exception as e:
                    self.weight_dict = {'Алгебра': [60, 25, 15],
                                        'Биология': [70, 5, 25],
                                        'География': [70, 10, 20],
                                        'Геометрия': [60, 25, 15],
                                        'Иностранный язык': [50, 30, 20],
                                        'Информатика': [60, 20, 20],
                                        'История': [40, 20, 40],
                                        'Литература': [40, 20, 40],
                                        'Обществознание': [60, 20, 20],
                                        'Русский язык': [40, 20, 40],
                                        'Физика': [70, 20, 10],
                                        'Физическая культура': [34, 33, 33],
                                        'Химия': [70, 20, 10]}

                # self.num_1.clicked.connect(self.run)
            # ввод чисел
            [i.clicked.connect(self.read_and_count_marks) for i in
             self.buttonGroup.buttons()]
            # установка значения "добавить" по умолчанию
            self.add_button.setChecked(True)
            # подключение к, ф, т
            self.pushButton_k.clicked.connect(self.k_pusher)
            self.pushButton_f.clicked.connect(self.f_pusher)
            self.pushButton_t.clicked.connect(self.t_pusher)
            # Сброс
            self.delete_all.clicked.connect(self.delete_all_func)
            # Настройки
            self.settings.clicked.connect(self.settings_func)
            # для дальнейшего исправления добавленных предметов
            self.subjects = list(self.mark_dict.keys())
            # combobox
            self.choose_subject.addItems(self.subjects)
            self.choose_subject.activated[str].connect(self.onActivated)
            # сохранить вес
            self.save_weight.clicked.connect(self.save_weight_funk)
            self.save_marks.clicked.connect(self.save_marks_func)
            self.subject = self.subjects[0]
            self.spinBox_k.setValue(self.weight_dict[self.subject][0])
            self.spinBox_f.setValue(self.weight_dict[self.subject][1])
            self.spinBox_t.setValue(self.weight_dict[self.subject][2])
            self.set_text(self.mark_dict[self.subject])
            # Автоматически стоит ввод формирующих оценок
            self.pushButton_f.setStyleSheet('QPushButton {background-color: #87CEEB; color: blue;}')
            self.mark_flag = 2
            self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')


        except Exception as e:
            print('init', e)


    # функция ввода, показа и подсчета оценок
    def read_and_count_marks(self):
        try:
            if self.mark_flag == 1:
                m_type = 'k'
            elif self.mark_flag == 2:
                m_type = 'f'
            else:
                m_type = 't'
            marks = self.mark_dict[self.subject]
            # Добавить/Убрать
            if self.add_button.isChecked():
                marks['new'][m_type].append(int(self.sender().text()))
            if self.remove_button.isChecked():
                if int(self.sender().text()) in marks['new'][m_type]:
                    marks['new'][m_type].remove(int(self.sender().text()))
                elif int(self.sender().text()) in marks['save'][m_type]:
                    marks['saved'][m_type].remove(int(self.sender().text()))
            # Вывод
            k = (((sum(marks['new']['k']) + sum(marks['saved']['k'])
                   ) / (len(marks['new']['k']) + len(marks['saved']['k'])))
                 if len(marks['new']['k']) + len(marks['saved']['k']) != 0 else 0) \
                * self.weight_dict[self.subject][0] / 100
            f = (((sum(marks['new']['f']) + sum(marks['saved']['f'])
                   ) / (len(marks['new']['f']) + len(marks['saved']['f'])))
                 if len(marks['new']['f']) + len(marks['saved']['f']) != 0 else 0) \
                * self.weight_dict[self.subject][1] / 100
            t = (((sum(marks['new']['t']) + sum(marks['saved']['t'])
                   ) / (len(marks['new']['t']) + len(marks['saved']['t'])))
                 if len(marks['new']['t']) + len(marks['saved']['t']) != 0 else 0) \
                * self.weight_dict[self.subject][2] / 100
            self.display.display(round(k + f + t, 2))
            self.set_text(marks)
        except Exception as e:
            print('read_and_count', e)

    # Вывод всех оценок
    def set_text(self, marks):
        self.textBrowser.setPlainText('''Констатирующая\nsaved: {}\nnew: {} \n\nФормирующая\nsaved: {}\nnew: {} \n\nТворческая\nsaved: {}\nnew: {} \n'''.format(
            ' '.join(map(str, marks['saved']['k'])), ' '.join(map(str, marks['new']['k'])),
            ' '.join(map(str, marks['saved']['f'])), ' '.join(map(str, marks['new']['f'])),
            ' '.join(map(str, marks['saved']['t'])), ' '.join(map(str, marks['new']['t']))))


    # подсчет после нажатия, radiobutton через pushputton, так красивее, вместо проверки кнопки провека флага
    def k_pusher(self):
        try:
            if self.pushButton_k.sender():
                self.pushButton_k.setStyleSheet('QPushButton {background-color: #F08080; color: #800000;}')
                self.mark_flag = 1
                self.pushButton_f.setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')
        except Exception as e:
            print('k_pusher', e)

    def f_pusher(self):
        try:
            if self.pushButton_f.sender():
                self.pushButton_f.setStyleSheet('QPushButton {background-color: #87CEEB; color: blue;}')
                self.mark_flag = 2
                self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')
        except Exception as e:
            print('f_pusher', e)

    def t_pusher(self):
        try:
            if self.pushButton_t.sender():
                self.pushButton_t.setStyleSheet('QPushButton {background-color: #98FB98; color: #008000;}')
                self.mark_flag = 3
                self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.pushButton_f.setStyleSheet('QPushButton {background-color: white; color: black;}')
        except Exception as e:
            print('t_pusher', e)

    # кобмобокс
    def onActivated(self, text):
        try:
            self.subject = text
            self.spinBox_k.setValue(self.weight_dict[self.subject][0])
            self.spinBox_f.setValue(self.weight_dict[self.subject][1])
            self.spinBox_t.setValue(self.weight_dict[self.subject][2])
            marks = self.mark_dict[self.subject]
            k = (((sum(marks['new']['k']) + sum(marks['saved']['k'])
                   ) / (len(marks['new']['k']) + len(marks['saved']['k'])))
                 if len(marks['new']['k']) + len(marks['saved']['k']) != 0 else 0) \
                * self.weight_dict[self.subject][0] / 100
            f = (((sum(marks['new']['f']) + sum(marks['saved']['f'])
                   ) / (len(marks['new']['f']) + len(marks['saved']['f'])))
                 if len(marks['new']['f']) + len(marks['saved']['f']) != 0 else 0) \
                * self.weight_dict[self.subject][1] / 100
            t = (((sum(marks['new']['t']) + sum(marks['saved']['t'])
                   ) / (len(marks['new']['t']) + len(marks['saved']['t'])))
                 if len(marks['new']['t']) + len(marks['saved']['t']) != 0 else 0) \
                * self.weight_dict[self.subject][2] / 100

            self.display.display(round(k + f + t, 2))
            self.set_text(marks)
        except Exception as e:
            print('onActivated', e)

    # сохранить вес
    def save_weight_funk(self):
        try:
            k = self.spinBox_k.value()
            f = self.spinBox_f.value()
            t = self.spinBox_t.value()
            assert k + f + t == 100
            self.weight_dict[self.subject] = [k, f, t]


        except AssertionError:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Неверный вес оценок. Вес каждой оценки задается в процентах. '
                        'Суммарный вес всех оценок должен быть равен 100')
            msg.setWindowTitle('Error')
            msg.show()
        except Exception as e:
            print('sav_weight', e)

    def save_marks_func(self):
        try:

            self.mark_dict[self.subject]['saved']['k'] += self.mark_dict[self.subject]['new']['k']
            self.mark_dict[self.subject]['saved']['f'] += self.mark_dict[self.subject]['new']['f']
            self.mark_dict[self.subject]['saved']['t'] += self.mark_dict[self.subject]['new']['t']
            self.mark_dict[self.subject]['new']['k'] = []
            self.mark_dict[self.subject]['new']['f'] = []
            self.mark_dict[self.subject]['new']['t'] = []
            self.set_text(self.mark_dict[self.subject])
        except Exception as e:
            print('save_marks', e)

    def delete_all_func(self):
        for j in self.mark_dict[self.subject]:
            for q in self.mark_dict[self.subject][j]:
                self.mark_dict[self.subject][j][q] = []
        self.set_text(self.mark_dict[self.subject])
        self.display.display(round(0, 2))

    # Открытие нового окна настроек
    def settings_func(self):
        try:
            self.sw = SettingWidget(self.mark_dict, self.weight_dict)
            self.sw.show()
            self.auto = True
            self.close()
        except Exception as e:
            print(e)

    # Отслеживание закрытия
    def closeEvent(self, event):
        try:
            if self.auto:
                event.accept()
            else:
                reply = QMessageBox.question(
                    self, 'Информация', "Вы уверены, что хотите выйти?",
                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    with open('weight.json', mode='w', encoding='utf-8') as file:
                        file.write(json.dumps(self.weight_dict))
                    with open('marks.json', mode='w', encoding='utf-8') as file:
                        a = json.dumps(self.mark_dict)
                        file.write(a)
                    event.accept()
                else:
                    event.ignore()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())