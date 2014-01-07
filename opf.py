# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opf.ui'
#
# Created: Tue Jan 07 12:14:35 2014
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
        openfd.resize(427, 456)
        self.gridLayout = QtGui.QGridLayout(openfd)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(openfd)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_number = QtGui.QLineEdit(openfd)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_number.sizePolicy().hasHeightForWidth())
        self.lineEdit_number.setSizePolicy(sizePolicy)
        self.lineEdit_number.setObjectName(_fromUtf8("lineEdit_number"))
        self.horizontalLayout.addWidget(self.lineEdit_number)
        self.lineEdit_name = QtGui.QLineEdit(openfd)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy)
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(openfd)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(openfd)
        self.plainTextEdit.setDocumentTitle(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 3, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(openfd)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(openfd)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtGui.QLineEdit(openfd)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 1, 1, 1)

        self.retranslateUi(openfd)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), openfd.close)
        QtCore.QMetaObject.connectSlotsByName(openfd)

    def retranslateUi(self, openfd):
        openfd.setWindowTitle(_translate("openfd", "匯入名單", None))
        self.label_4.setText(_translate("openfd", "請輸入本名單的欄位標題", None))
        self.lineEdit_number.setText(_translate("openfd", "學號", None))
        self.lineEdit_number.setPlaceholderText(_translate("openfd", "預設為學號", None))
        self.lineEdit_name.setText(_translate("openfd", "姓名", None))
        self.plainTextEdit.setToolTip(_translate("openfd", "請用 tab 鍵分隔學號姓名", None))
        self.label_2.setText(_translate("openfd", "總人數", None))
        self.label_3.setText(_translate("openfd", "檔案名稱", None))
        self.lineEdit.setToolTip(_translate("openfd", "輸入的名稱將作為主程式中的名單名稱", None))
        self.lineEdit.setPlaceholderText(_translate("openfd", "存檔前請先指定名稱", None))

