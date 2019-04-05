# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwerty.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_subject = QtWidgets.QComboBox(self.centralwidget)
        self.choose_subject.setGeometry(QtCore.QRect(20, 10, 191, 41))
        self.choose_subject.setObjectName("choose_subject")
        self.display = QtWidgets.QLCDNumber(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(230, 10, 191, 41))
        self.display.setObjectName("display")
        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(230, 120, 51, 51))
        self.num_2.setObjectName("num_2")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.num_2)
        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(300, 120, 51, 51))
        self.num_1.setObjectName("num_1")
        self.buttonGroup.addButton(self.num_1)
        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        self.num_0.setGeometry(QtCore.QRect(370, 120, 51, 51))
        self.num_0.setObjectName("num_0")
        self.buttonGroup.addButton(self.num_0)
        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setGeometry(QtCore.QRect(300, 60, 51, 51))
        self.num_4.setObjectName("num_4")
        self.buttonGroup.addButton(self.num_4)
        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setGeometry(QtCore.QRect(370, 60, 51, 51))
        self.num_3.setObjectName("num_3")
        self.buttonGroup.addButton(self.num_3)
        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setGeometry(QtCore.QRect(230, 60, 51, 51))
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
        self.save_weight.setObjectName("save_weight")
        self.add_button = QtWidgets.QRadioButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(230, 180, 101, 51))
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
        self.save_marks.setObjectName("save_marks")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 300, 401, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.spinBox_k = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_k.setGeometry(QtCore.QRect(90, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_k.setFont(font)
        self.spinBox_k.setObjectName("spinBox_k")
        self.spinBox_f = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_f.setGeometry(QtCore.QRect(90, 120, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_f.setFont(font)
        self.spinBox_f.setObjectName("spinBox_f")
        self.spinBox_t = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_t.setGeometry(QtCore.QRect(90, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_t.setFont(font)
        self.spinBox_t.setObjectName("spinBox_t")
        self.pushButton_k = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_k.setGeometry(QtCore.QRect(20, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_k.setFont(font)
        self.pushButton_k.setObjectName("pushButton_k")
        self.pushButton_f = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_f.setGeometry(QtCore.QRect(20, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_f.setFont(font)
        self.pushButton_f.setObjectName("pushButton_f")
        self.pushButton_t = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_t.setGeometry(QtCore.QRect(20, 180, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_t.setFont(font)
        self.pushButton_t.setObjectName("pushButton_t")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Сохраненные оценки. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Ф 1 2 3 4 5 4 2  2 3 2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">К 1 3 4  2 3 3 3 3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Т 3 3 4 4 4  3 4 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Добавленные оценки.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Ф 5 4 3  2 5 7 7 6 3 5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">К 4 5 2 4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">Т 4 5 7 9 5 5</span></p></body></html>"))
        self.pushButton_k.setText(_translate("MainWindow", "К"))
        self.pushButton_f.setText(_translate("MainWindow", "Ф"))
        self.pushButton_t.setText(_translate("MainWindow", "Т"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        

        # для дальнейшего исправления добавленных предметов
        self.subjects = ['Алгебра',
                         'Биология',
                         'География',
                         'Геометрия',
                         'Иностранный язык',
                         'Информатика',
                         'История',
                         'Литература',
                         'Обществознание',
                         'Русский язык',
                         'Физика',
                         'Физическая культура',
                         'Химия']
        
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
        # combobox
        self.choose_subject.addItems(self.subjects)
        self.choose_subject.activated[str].connect(self.onActivated)
        
        # сохранить вес
        self.save_weight.clicked.connect(self.save_weight_funk)

        # sorry for sps но я должна была, если что исправим потом
        self.sps = []
        self.mark_flag = None
        self.k_res = 0
        self.f_res = 0
        self.t_res = 0
        self.subject = self.subjects[0]

    # функция ввода, показа и подсчета оценок
    def read_and_count_marks(self):
        # потом я подгоню это все под разные оценки с помощью всяких флагов
        if self.add_button.isChecked():
            self.sps.append(int(self.sender().text()))
        if self.remove_button.isChecked():
            self.sps.remove(int(self.sender().text()))
        # работа с флагами после подключения чекбоксов
        self.display.display(round(sum(self.sps) / len(self.sps), 2))


    # подсчет после нажатия, radiobutton через pushputton, так красивее, вместо проверки кнопки провека флага
    def k_pusher(self):
        if self.pushButton_k.sender():
            self.pushButton_k.setStyleSheet('QPushButton {background-color: #F08080; color: #800000;}')
            self.mark_flag = 1
            self.pushButton_f.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')
            
            
    def f_pusher(self):
        if self.pushButton_f.sender():
            self.pushButton_f.setStyleSheet('QPushButton {background-color: #87CEEB; color: blue;}')
            self.mark_flag = 2
            self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')
            
            
    def t_pusher(self):
        if self.pushButton_t.sender():
            self.pushButton_t.setStyleSheet('QPushButton {background-color: #98FB98; color: #008000;}')
            self.mark_flag = 3
            self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.pushButton_f.setStyleSheet('QPushButton {background-color: white; color: black;}')
            
    # кобмобокс
    def onActivated(self, text):
        self.subject = text
        
    
    # сохранить вес
    def save_weight_funk(self):
        self.weight_dict[self.subject] = [self.spinBox_k.value(), self.spinBox_f.value(), self.spinBox_t.value()]
        
        
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
