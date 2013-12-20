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
        self.opfpushButton.clicked.connect(self.browsef)

        iconop = QtGui.QIcon()
        iconop.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opfpushButton.setIcon(iconop)
        # a.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # a.setArrowType(Qt.NoArrow)
        self.show()
    def browsef(self):
        cwd = os.getcwdu()
        print cwd
        self.desktopPath = QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.DesktopLocation)
        fname = QtGui.QFileDialog.getOpenFileName(self,'open file',self.desktopPath,"txt file (*.txt *.csv)")
        fname = unicode(fname)
        print fname
        #命名
        a = dict()
        with open(fname, mode='r') as infile:
        #想想看如何自動偵測編碼
            self.content = infile.read().lstrip("\n").rstrip("\n")
            # try:
            print self.content.decode("utf-16le")
            #     coding = 'cp950'
            # except UnicodeDecodeError:
            #     print self.content.decode("utf-16")
            #     coding = 'utf-16'
            # else:
            #     try:
            #         print self.content.decode('utf-8')
            #         coding = 'utf-8'
            #     except UnicodeDecodeError:
            #         pass
            # finally:
            #     print(coding)



            self.content = self.content.decode(coding).split('\n')
            lens = len(self.content)
            for row in self.content:
                row = row.split('\t')
                a[row[0]] = row[1]
        print a
        self.textBrowser.setText("\n".join(self.content))
        self.label_2.setText(str(lens))
        self.buttonBox.accepted.connect(self.savef)

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
                fh.write("\n".join(self.content).encode('utf-8'))
            QtGui.QMessageBox.information(None, u"成功",
                            u"名單匯入成功，\n請重新啟動程式",
                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                            QtGui.QMessageBox.NoButton)
            self.buttonBox.accepted.connect(self.close())



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = opf()
    sys.exit(app.exec_())