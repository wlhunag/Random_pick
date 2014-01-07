# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del.ui'
#
# Created: Tue Jan 07 12:24:11 2014
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

class Ui_delform(object):
    def setupUi(self, delform):
        delform.setObjectName(_fromUtf8("delform"))
        delform.resize(253, 245)
        self.delbtn = QtGui.QPushButton(delform)
        self.delbtn.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.delbtn.setObjectName(_fromUtf8("delbtn"))
        self.listView = QtGui.QListView(delform)
        self.listView.setGeometry(QtCore.QRect(20, 40, 141, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(delform)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.finebtn = QtGui.QPushButton(delform)
        self.finebtn.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.finebtn.setObjectName(_fromUtf8("finebtn"))

        self.retranslateUi(delform)
        QtCore.QMetaObject.connectSlotsByName(delform)

    def retranslateUi(self, delform):
        delform.setWindowTitle(_translate("delform", "刪除名單", None))
        self.delbtn.setText(_translate("delform", "刪除", None))
        self.label.setText(_translate("delform", "目前現有名單", None))
        self.finebtn.setText(_translate("delform", "完成", None))

