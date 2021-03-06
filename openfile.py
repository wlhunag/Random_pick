#-*- coding: utf-8-*-
__author__ = 'Aaron'
import sys
import os
import codecs
from PyQt4 import QtGui
from opf import Ui_openfd

class opf(QtGui.QDialog,Ui_openfd):
    def __init__(self,parent=None):
        super(opf, self).__init__(parent)
        self.setupUi(self)

        self.show()
        self.plainTextEdit.acceptDrops()
        self.plainTextEdit.textChanged.connect(self.cunt)
        self.buttonBox.accepted.connect(self.savef)

    def cunt(self):
        self.text = unicode(self.plainTextEdit.toPlainText()).encode('utf-8').lstrip("\n").rstrip("\n")
        num =  self.text.count('\n') + 1
        self.label_2.setText(str(num))

    def savef(self):
        cwd = os.getcwdu()
        fn = unicode(self.lineEdit.text())
        if fn == u'':
            QtGui.QMessageBox.critical(None, u"沒檔名",
                            u"存檔前請輸入檔名",
                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                            QtGui.QMessageBox.NoButton)
        else:
            newl = os.path.join(cwd,"namelist",fn)

            with open(newl,'w') as fh:
            #    print(u"新名單內容為"),
             #   print(unicode(self.plainTextEdit.toPlainText()))
                fh.write(unicode(self.lineEdit_number.text()).encode('utf-8') + '\t' + unicode(self.lineEdit_name.text()).encode('utf-8') + '\n')
                fh.write(unicode(self.plainTextEdit.toPlainText()).encode('utf-8').lstrip("\n").rstrip("\n"))
            QtGui.QMessageBox.information(None, u"成功",
                            u"名單匯入成功，\n請重新啟動程式",
                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                            QtGui.QMessageBox.NoButton)
            # self.buttonBox.accepted.connect(lambda :self.close())
            self.close()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = opf()
    sys.exit(app.exec_())