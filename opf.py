# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opf.ui'
#
# Created: Sun Dec 29 08:14:44 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_openfd(object):
    def setupUi(self, openfd):
        openfd.setObjectName(_fromUtf8("openfd"))
        openfd.resize(376, 385)
        self.buttonBox = QtGui.QDialogButtonBox(openfd)
        self.buttonBox.setGeometry(QtCore.QRect(220, 320, 156, 23))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(openfd)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 239, 151, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(openfd)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 210, 121, 21))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.plainTextEdit = QtGui.QPlainTextEdit(openfd)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 90, 201, 251))
        self.plainTextEdit.setDocumentTitle(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(openfd)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 201, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_number = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_number.setObjectName(_fromUtf8("lineEdit_number"))
        self.horizontalLayout.addWidget(self.lineEdit_number)
        self.lineEdit_name = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.label_4 = QtGui.QLabel(openfd)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 201, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(openfd)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), openfd.close)
        QtCore.QMetaObject.connectSlotsByName(openfd)

    def retranslateUi(self, openfd):
        openfd.setWindowTitle(_translate("openfd", "匯入名單", None))
        self.label_3.setText(_translate("openfd", "名稱", None))
        self.lineEdit.setToolTip(_translate("openfd", "輸入的名稱將作為主程式中的名單名稱", None))
        self.lineEdit.setPlaceholderText(_translate("openfd", "存檔前請先指定名稱", None))
        self.label.setText(_translate("openfd", "總人數", None))
        self.plainTextEdit.setToolTip(_translate("openfd", "請用 tab 鍵分隔學號姓名", None))
        self.lineEdit_number.setText(_translate("openfd", "學號", None))
        self.lineEdit_number.setPlaceholderText(_translate("openfd", "要輸入標題喔", None))
        self.lineEdit_name.setText(_translate("openfd", "姓名", None))
        self.label_4.setText(_translate("openfd", "請輸入本名單的欄位標題", None))

