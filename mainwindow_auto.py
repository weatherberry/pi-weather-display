# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.centralWidget.setPalette(palette)
        self.centralWidget.setAutoFillBackground(True)
        self.centralWidget.setObjectName("centralWidget")
        self.lblTemperature = QtWidgets.QLabel(self.centralWidget)
        self.lblTemperature.setGeometry(QtCore.QRect(210, 329, 571, 161))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(120)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lblTemperature.setFont(font)
        self.lblTemperature.setTextFormat(QtCore.Qt.AutoText)
        self.lblTemperature.setScaledContents(False)
        self.lblTemperature.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lblTemperature.setObjectName("lblTemperature")
        self.lblHumidity = QtWidgets.QLabel(self.centralWidget)
        self.lblHumidity.setGeometry(QtCore.QRect(441, 187, 341, 141))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lblHumidity.setFont(font)
        self.lblHumidity.setTextFormat(QtCore.Qt.AutoText)
        self.lblHumidity.setScaledContents(False)
        self.lblHumidity.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lblHumidity.setObjectName("lblHumidity")
        self.lblLightLevel = QtWidgets.QLabel(self.centralWidget)
        self.lblLightLevel.setGeometry(QtCore.QRect(30, 30, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.lblLightLevel.setFont(font)
        self.lblLightLevel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblLightLevel.setObjectName("lblLightLevel")
        self.lblSmokeLevel = QtWidgets.QLabel(self.centralWidget)
        self.lblSmokeLevel.setGeometry(QtCore.QRect(30, 70, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.lblSmokeLevel.setFont(font)
        self.lblSmokeLevel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblSmokeLevel.setObjectName("lblSmokeLevel")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTemperature.setText(_translate("MainWindow", "--,- °C"))
        self.lblHumidity.setText(_translate("MainWindow", "Feuchtigkeit: --%"))
        self.lblLightLevel.setText(_translate("MainWindow", "Es ist 50% hell draußen."))
        self.lblSmokeLevel.setText(_translate("MainWindow", "Smoke level:"))

