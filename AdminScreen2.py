# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminScreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from CreateAnimalScreen import Ui_MainWindow
from LoginScreen import Ui_Dialog

class Ui_adminScreen(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLogin(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, adminScreen):
        adminScreen.setObjectName("adminScreen")
        adminScreen.resize(465, 341)
        self.label = QtWidgets.QLabel(adminScreen)
        self.label.setGeometry(QtCore.QRect(170, 10, 121, 16))
        self.label.setObjectName("label")

        self.logoutBtn = QtWidgets.QPushButton(adminScreen)
        self.logoutBtn.setGeometry(QtCore.QRect(340, 130, 75, 23))
        self.logoutBtn.setObjectName("logoutBtn")
        self.logoutBtn.clicked.connect(self.openLogin)

        self.graphicsView = QtWidgets.QGraphicsView(adminScreen)
        self.graphicsView.setGeometry(QtCore.QRect(320, 20, 121, 101))
        self.graphicsView.setObjectName("graphicsView")

        self.view_database_btn = QtWidgets.QPushButton(adminScreen)
        self.view_database_btn.setGeometry(QtCore.QRect(20, 80, 261, 61))
        self.view_database_btn.setObjectName("view_database_btn")


        self.add_animal_btn = QtWidgets.QPushButton(adminScreen)
        self.add_animal_btn.setGeometry(QtCore.QRect(20, 150, 261, 61))
        self.add_animal_btn.setObjectName("add_animal_btn")
        self.add_animal_btn.clicked.connect(self.openWindow)

        self.retranslateUi(adminScreen)
        QtCore.QMetaObject.connectSlotsByName(adminScreen)

    def retranslateUi(self, adminScreen):
        _translate = QtCore.QCoreApplication.translate
        adminScreen.setWindowTitle(_translate("adminScreen", "Dialog"))
        self.label.setText(_translate("adminScreen", "Welcome - Administrator"))
        self.logoutBtn.setText(_translate("adminScreen", "Log Out"))
        self.view_database_btn.setText(_translate("adminScreen", "View Database"))
        self.add_animal_btn.setText(_translate("adminScreen", "Add New Animal"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminScreen = QtWidgets.QDialog()
    ui = Ui_adminScreen()
    ui.setupUi(adminScreen)
    adminScreen.show()
    sys.exit(app.exec_())

