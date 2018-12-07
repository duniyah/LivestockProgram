# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 429)
        self.databasetable = QtWidgets.QTableWidget(Dialog)
        self.databasetable.setGeometry(QtCore.QRect(10, 60, 531, 281))
        self.databasetable.setRowCount(14)
        self.databasetable.setColumnCount(5)
        self.databasetable.setObjectName("databasetable")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 20, 81, 21))
        self.label.setObjectName("label")
        self.loadBtn = QtWidgets.QPushButton(Dialog)
        self.loadBtn.setGeometry(QtCore.QRect(240, 370, 75, 23))
        self.loadBtn.setObjectName("loadBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Animal Database"))
        self.loadBtn.setText(_translate("Dialog", "Reload Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

