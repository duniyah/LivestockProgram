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
#from AdminScreen1 import Ui_createReportBtn
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

                created = 1

            except mariadb.Error as error:
                print("connection failed")
                sys.exit(1)
            mariadb_connection.commit()

        except mariadb.Error as error:
            print("Error: {}".format(error))
        print("check")

    def _str_handler_signup(self):
        """
        This code handles input and tracks errors
        """

        #current = self.user.text()
        fname = str(self.firstName.text())
        lname = str(self.lastName.text())
        accountUser = str(self.username_2.text())
        accountPass = str(self.password_2.text())
        accountEmail = str(self.emailAdd.text())
        accountConfirm = str(self.confirmPass.text())
        try:
            # new_value1 = fname.strip()
            # new_value2 = lname.strip()
            # new_value3 = accountUser.strip()
            # new_value4 = accountPass.strip()
            new_value1 = accountPass.strip()
            new_value2 = accountConfirm.strip()
            if new_value1 == "":
                raise ValueError
            color1 = "#FFFFFF"
            self._current_value = new_value1
            self._valid = True

            if new_value2 == "":
                raise ValueError
            color2 = "#FFFFFF"
            self._current_value = new_value2
            self._valid = True

        except ValueError:
            color1 = "#FFB6C1"
            color2 = "#FFB6C1"
            self._valid = False
            if color1 == color2:
                QMessageBox.question(self, 'Password Error', "Your passwords do not match. Please re-enter information " , QMessageBox.Ok,
                                     QMessageBox.Ok)
                self.textbox.setText("")

        self.password_2.setStyleSheet("QLineEdit {{ background-color: {} }}".format(color1))
        self.confirmPass.setStyleSheet("QLineEdit {{ background-color: {} }}".format(color2))

    def loginMethod(self):
        username_log = str(self.username.text())
        password_log = str(self.password.text())
        print(username_log, password_log)
        try:
            check_userinfo = (
                "SELECT user_name, user_password FROM userinformation WHERE user_name = %s AND user_password = %s")
            print('queried')
            user_logindata = (username_log, password_log)
            cursor.execute(check_userinfo, (username_log, password_log))
            myresult = cursor.fetchall()
            for x in myresult:
                print(x)

            login = 1

        except mariadb.Error as error:
            print("connection failed")
            sys.exit(1)
        mariadb_connection.commit()

    def openAdminScreen(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_createReportBtn()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

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
        self.loginBtn.clicked.connect(self.loginMethod)

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


