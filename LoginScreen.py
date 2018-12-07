# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QAbstractButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import MySQLdb
import mysql.connector as mariadb

class Ui_Dialog(object):

    def connectDatabase(self):
        try:
            mariadb_connection = mariadb.connect(user='root', password='', database='livestocktest')
            cursor = mariadb_connection.cursor()
            print("connection successful")

        except mariadb.Error as error:
            print("connection failed")
            sys.exit(1)

    def openAdminScreen(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_adminScreen()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def createAccount(self):

        fname = str(self.firstName.text())
        lname = str(self.lastName.text())
        accountUser = str(self.username_2.text())
        accountPass = str(self.password_2.text())
        accountEmail = str(self.emailAdd.text())
        accountConfirm = str(self.confirmPass.text())
        print(fname, lname, accountUser, accountEmail, accountPass, accountConfirm)
        try:
            mariadb_connection = mariadb.connect(user='root', password='', database='livestocktest')
            cursor = mariadb_connection.cursor()
            print("connection successful")

            try:
                add_userinfo = (
                    "INSERT INTO userinformation (user_name, user_password, user_email, first_name, last_name) VALUES (%s,%s,%s,%s,%s)")
                print('inserted')
                user_data = (accountUser, accountPass, accountEmail, fname, lname)
                cursor.execute(add_userinfo, user_data)

                for first_name, last_name in cursor:
                    print("First name: {}, Last name: {}").format(first_name, last_name)

                # created = 1
                # if created == 1:
                #     openAdminScreen()

            except mariadb.Error as error:
                print("connection failed")
                sys.exit(1)
            mariadb_connection.commit()

        except mariadb.Error as error:
            print("Error: {}".format(error))
        print("check")

    def _str_handler(self):
        """
        This code handles input and tracks errors
        """
        username_log = str(self.username.text())
        password_log = str(self.password.text())
        try:
            new_value1 = username_log.strip()
            if new_value1 == "":
                raise ValueError
            color1 = "#FFFFFF"
            self._current_value1 = new_value1
            self._valid1 = True
        except ValueError:
            color1 = "#FFB6C1"
            self._valid1 = False

        self.username.setStyleSheet("QLineEdit {{ background-color: {} }}".format(color1))

        try:
            new_value2 = password_log.strip()
            if new_value2 == "":
                raise ValueError
            color2 = "#FFFFFF"
            self._current_value2 = new_value2
            self._valid2 = True
        except ValueError:
            color2 = "#FFB6C1"
            self._valid2 = False

        self.password.setStyleSheet("QLineEdit {{ background-color: {} }}".format(color2))

    def loginMethod(self):
        try:
            cnx = mariadb.connect(user='root', password='', database='livestocktest')
            cursor = cnx.cursor()

            query = ("SELECT user_name, user_password FROM userinformation "
                     "WHERE user_name = %s AND user_password = %s")

            username_log = str(self.username.text())
            password_log = str(self.password.text())
            info = (username_log, password_log)

            cursor.execute(query, (info))
            valid = 1
            print(valid)

            for (first_name, last_name) in cursor:
                print("{}, {} was hired".format(
                    last_name, first_name))

        except mariadb.Error as error:
            print("connection failed")
            sys.exit(1)

    # def openAdminScreen(self):
    #     self.dialog = QtWidgets.QDialog()
    #     self.ui = Ui_createReportBtn()
    #     self.ui.setupUi(self.dialog)
    #     self.dialog.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 91, 31))
        self.label.setObjectName("label")

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 391, 271))

        #code for the signup tab
        self.tabWidget.setObjectName("tabWidget")
        self.signupTab = QtWidgets.QWidget()
        self.signupTab.setObjectName("signupTab")
        self.label_4 = QtWidgets.QLabel(self.signupTab)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.signupTab)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.signupTab)
        self.label_6.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.label_6.setObjectName("label_6")


        self.createBtn = QtWidgets.QPushButton(self.signupTab)
        self.createBtn.setGeometry(QtCore.QRect(90, 210, 91, 23))
        self.createBtn.setObjectName("createBtn")
        self.createBtn.clicked.connect(self.createAccount)
        # self.createBtn.clicked(self.openAdminScreen)

        self.label_7 = QtWidgets.QLabel(self.signupTab)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.signupTab)
        self.label_8.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.signupTab)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 91, 16))
        self.label_9.setObjectName("label_9")

        self.firstName = QtWidgets.QLineEdit(self.signupTab)
        self.firstName.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.firstName.setObjectName("firstName")

        self.lastName = QtWidgets.QLineEdit(self.signupTab)
        self.lastName.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lastName.setObjectName("lastName")

        self.confirmPass = QtWidgets.QLineEdit(self.signupTab)
        self.confirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPass.setGeometry(QtCore.QRect(130, 180, 113, 20))
        self.confirmPass.setObjectName("confirmPass")

        self.password_2 = QtWidgets.QLineEdit(self.signupTab)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.password_2.setObjectName("password_2")

        self.username_2 = QtWidgets.QLineEdit(self.signupTab)
        self.username_2.setGeometry(QtCore.QRect(130, 120, 113, 20))
        self.username_2.setObjectName("username_2")

        self.emailAdd = QtWidgets.QLineEdit(self.signupTab)
        self.emailAdd.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.emailAdd.setObjectName("emailAdd")

        self.cancelBtn_2 = QtWidgets.QPushButton(self.signupTab)
        self.cancelBtn_2.setGeometry(QtCore.QRect(220, 210, 91, 23))
        self.cancelBtn_2.setObjectName("cancelBtn_2")
        self.cancelBtn_2.clicked.connect(self.closeApp)


        #Code for the Login Tab
        self.tabWidget.addTab(self.signupTab, "")
        self.Lo = QtWidgets.QWidget()
        self.Lo.setObjectName("Lo")

        self.password = QtWidgets.QLineEdit(self.Lo)
        self.password.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_3 = QtWidgets.QLabel(self.Lo)
        self.label_3.setGeometry(QtCore.QRect(90, 80, 47, 13))
        self.label_3.setObjectName("label_3")

        self.loginBtn = QtWidgets.QPushButton(self.Lo)
        self.loginBtn.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self._str_handler)
        self.loginBtn.clicked.connect(self.loginMethod)
        self.loginBtn.clicked.connect(self.openAdminScreen)

        self.username = QtWidgets.QLineEdit(self.Lo)
        self.username.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.username.setObjectName("username")

        self.label_2 = QtWidgets.QLabel(self.Lo)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 47, 13))
        self.label_2.setObjectName("label_2")

        self.cancelBtn = QtWidgets.QPushButton(self.Lo)
        self.cancelBtn.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.clicked.connect(self.closeApp)

        self.tabWidget.addTab(self.Lo, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_4.setText(_translate("Dialog", "First Name"))
        self.label_5.setText(_translate("Dialog", "Last Name"))
        self.label_6.setText(_translate("Dialog", "Email Address"))
        self.createBtn.setText(_translate("Dialog", "Create Account"))

        self.label_7.setText(_translate("Dialog", "Username"))
        self.label_8.setText(_translate("Dialog", "Password"))
        self.label_9.setText(_translate("Dialog", "Confirm Password"))
        self.cancelBtn_2.setText(_translate("Dialog", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.signupTab), _translate("Dialog", "Create Account"))

        self.label_3.setText(_translate("Dialog", "Password"))
        self.loginBtn.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Lo), _translate("Dialog", "Log In"))

    def closeApp(self):
        sys.exit(1)

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.animaltypeBox = QtWidgets.QComboBox(self.centralwidget)
        self.animaltypeBox.setGeometry(QtCore.QRect(150, 50, 181, 22))
        self.animaltypeBox.setObjectName("animaltypeBox")
        self.animaltypeBox.addItem("")
        self.animaltypeBox.addItem("")
        self.animaltypeBox.addItem("")
        self.animaltypeBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 101, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 80, 181, 31))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 101, 16))
        self.label_2.setObjectName("label_2")
        self.genderBox = QtWidgets.QComboBox(self.centralwidget)
        self.genderBox.setGeometry(QtCore.QRect(150, 140, 181, 22))
        self.genderBox.setObjectName("genderBox")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 240, 101, 16))
        self.label_4.setObjectName("label_4")
        self.healthBox = QtWidgets.QComboBox(self.centralwidget)
        self.healthBox.setGeometry(QtCore.QRect(150, 260, 181, 22))
        self.healthBox.setObjectName("healthBox")
        self.healthBox.addItem("")
        self.healthBox.addItem("")
        self.healthBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 200, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(180, 310, 121, 23))
        self.saveBtn.setObjectName("saveBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 21))
        self.menubar.setObjectName("menubar")
        self.menuCreate_Animal = QtWidgets.QMenu(self.menubar)
        self.menuCreate_Animal.setObjectName("menuCreate_Animal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCreate_Animal.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.animaltypeBox.setItemText(0, _translate("MainWindow", "Cow"))
        self.animaltypeBox.setItemText(1, _translate("MainWindow", "Chicken"))
        self.animaltypeBox.setItemText(2, _translate("MainWindow", "Goat"))
        self.animaltypeBox.setItemText(3, _translate("MainWindow", "Sheep"))
        self.label.setText(_translate("MainWindow", "Select Animal Type"))
        self.label_2.setText(_translate("MainWindow", "Gender:"))
        self.genderBox.setItemText(0, _translate("MainWindow", "Male"))
        self.genderBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_3.setText(_translate("MainWindow", "Color:"))
        self.label_4.setText(_translate("MainWindow", "Health State:"))
        self.healthBox.setItemText(0, _translate("MainWindow", "Healthy"))
        self.healthBox.setItemText(1, _translate("MainWindow", "Sick"))
        self.healthBox.setItemText(2, _translate("MainWindow", "Pregnant"))
        self.saveBtn.setText(_translate("MainWindow", "Save Animal Entry"))
        self.menuCreate_Animal.setTitle(_translate("MainWindow", "Create Animal"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


