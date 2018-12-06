# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerScreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 326)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 130, 261, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.viewBtn = QtWidgets.QPushButton(Dialog)
        self.viewBtn.setGeometry(QtCore.QRect(30, 60, 261, 61))
        self.viewBtn.setObjectName("viewBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 121, 16))
        self.label.setObjectName("label")
        self.logoutBtn = QtWidgets.QPushButton(Dialog)
        self.logoutBtn.setGeometry(QtCore.QRect(350, 140, 75, 23))
        self.logoutBtn.setObjectName("logoutBtn")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(330, 30, 121, 101))
        self.graphicsView.setObjectName("graphicsView")
        self.createAnimal = QtWidgets.QPushButton(Dialog)
        self.createAnimal.setGeometry(QtCore.QRect(30, 200, 261, 61))
        self.createAnimal.setObjectName("createAnimal")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "Create Report"))
        self.viewBtn.setText(_translate("Dialog", "View Database and Update Animal Information"))
        self.label.setText(_translate("Dialog", "Welcome - Manager"))
        self.logoutBtn.setText(_translate("Dialog", "Log Out"))
        self.createAnimal.setText(_translate("Dialog", "Create New Animal Entry"))

