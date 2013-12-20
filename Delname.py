#-*- coding: utf-8-*-
__author__ = 'Aaron'
import sys
import os
from PyQt4 import QtGui
from delf import Ui_delform

class delf(QtGui.QDialog,Ui_delform):
    def __init__(self,parent =None):
        super(delf, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.start()
        self.finebtn.clicked.connect(self.finish)
        iconop = QtGui.QIcon()
        iconop.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delbtn.setIcon(iconop)


    def finish(self):
         QtGui.QMessageBox.information(None, u"成功",
                            u"名單刪除成功，\n請重新啟動程式",
                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                            QtGui.QMessageBox.NoButton)

         self.close()

    def start(self):
        model = QtGui.QStandardItemModel(self.listView)
        cwd = os.getcwdu()
        print cwd
        self.storelocation = os.path.join(cwd,"namelist")
        fs = os.listdir(self.storelocation)
        for f in fs:
            item = QtGui.QStandardItem(f)
            model.appendRow(item)
        self.listView.setModel(model)
        self.delbtn.clicked.connect(self.delaction)

    def delaction(self):
        for index in self.listView.selectedIndexes():
            a =  unicode(index.data().toString())
        import os
        rmf = os.path.join(self.storelocation,a)
        os.remove(rmf)
        self.start()




if __name__ =="__main__":
    app = QtGui.QApplication(sys.argv)
    window = delf()
    sys.exit(app.exec_())