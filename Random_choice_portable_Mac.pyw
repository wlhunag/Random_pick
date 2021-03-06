#-*- coding: utf-8-*-
__author__ = 'Aaron'
import os
import sys

from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QWidget, QMessageBox, QLabel, QSpinBox, QComboBox, \
    QToolButton, QHBoxLayout, QVBoxLayout, QIcon, QPixmap, QPushButton, QKeySequence, \
    QMenu, QTableWidgetItem, QTableWidget, QCursor, QAbstractItemView, QApplication


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.createLayout()
        self.updatenamelist()
        self.create_connection()
        # print u"目前所選的名單是",
        #似乎把 print 全都 comment 以後就可以無終端機執行了

        current_class = unicode(self.selectclass.currentText())

        if current_class == "":
            QMessageBox.warning(self, u"沒有名單喔", u"沒有名單喔\n抽籤以前！\n請新增名單吧~")
            self.add_group()

        else:
            fileLocation = os.path.join(os.getcwdu(), "namelist", current_class)
            self.whichClass = dict()
            with open(fileLocation, mode='r') as infile:
                #讀取第一行，當作欄位名稱，再將其餘當作資料內容
                self.title = infile.readline().lstrip("\n").rstrip("\n").decode('utf-8').split('\t')
                self.content = infile.read().lstrip("\n").rstrip("\n").decode('utf-8')
                self.content = self.content.split('\n')
                try:
                    for row in self.content:
                        row = row.split('\t')
                        self.whichClass[row[0]] = row[1]
                except IndexError:
                    QMessageBox.warning(self, u"名單有問題喔", u"'%s'名單有問題喔\n請重新啟動程式，再次匯入名單吧~" % current_class)
                    cwd = os.getcwdu()
                    infile.close()
                    if os.path.isfile(os.path.join(cwd, 'namelist', current_class)):
                        os.unlink(os.path.join(cwd, 'namelist', current_class))
                        sys.exit(0)

            self.allnumber = self.whichClass.keys()
        self.makedic()


    def createLayout(self):
        self.label = QLabel()
        self.label.setText(u"選出")
        self.label_2 = QLabel()
        self.label_2.setText(u"人")

        self.spinbox = QSpinBox()
        self.spinbox.size()

        self.spinbox.setValue(1)
        self.spinbox.sizeHint()

        self.labelA = QLabel(u"班級")
        self.selectclass = QComboBox()
        self.selectclass.setToolTip(u"中途切換班級會\n造成抽過的人還會被抽到\n就像是重新抽一樣")

        self.more = QToolButton()
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/gear.png"), QIcon.Normal, QIcon.Off)
        self.more.setIcon(icon)
        self.more.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.more.setArrowType(Qt.NoArrow)

        h1 = QHBoxLayout()
        h1.addWidget(self.label)
        h1.addWidget(self.spinbox)
        h1.addWidget(self.label_2)
        h1.addStretch()

        h4 = QHBoxLayout()
        h4.addStretch()
        h4.addWidget(self.labelA)
        h4.addWidget(self.selectclass)
        h4.addWidget(self.more)

        self.goButton = QPushButton("Go")
        self.goButton.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_G))
        self.goButton.setToolTip(u"開始抽抽樂 (Command + G )")
        icong = QIcon()
        icong.addPixmap(QPixmap("icons/dice.png"), QIcon.Normal, QIcon.Off)
        self.goButton.setIcon(icong)
        self.goButton.setFocus()
        self.clearButton = QPushButton("")
        self.clearButton.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.clearButton.setToolTip(u"清除...(Command + F)")
        iconc = QIcon()
        iconc.addPixmap(QPixmap("icons/eraser.png"), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(iconc)

        h2 = QHBoxLayout()
        h2.setMargin(1)
        h2.addWidget(self.goButton)
        h2.addWidget(self.clearButton)

        self.viewResultTable = QTableWidget(0, 2)
        self.viewResultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.viewResultTable.setColumnWidth(0, 130)
        self.viewResultTable.setColumnWidth(1, 123)

        self.viewResultTable.horizontalHeader().setToolTip(u"欄位標題根據匯入名單時的設定")

        self.viewResultTable.verticalHeader().hide()
        self.viewResultTable.setShowGrid(False)
        h3 = QVBoxLayout()
        h3.addWidget(self.viewResultTable)

        layout = QVBoxLayout()

        layout.addLayout(h1)

        layout.addLayout(h2)
        layout.addLayout(h3)
        layout.addLayout(h4)
        self.setLayout(layout)
        self.setWindowTitle(u"抽抽樂")
        self.setWindowIcon(QIcon("icons/Flaticon_1430.png"))


    def create_connection(self):
        self.goButton.clicked.connect(lambda: self.random_choice(self.spinbox.value()))
        self.clearButton.clicked.connect(lambda: self.del_old_table())
        self.connect(self.more, SIGNAL("clicked()"), self.moreac)
        self.more.setText(u"▾")
        self.selectclass.currentIndexChanged.connect(lambda: self.makedic())


    def updatenamelist(self):
        cwd = os.getcwdu()
        # print cwd
        self.storelocation = os.path.join(cwd, "namelist")
        if os.path.isfile(os.path.join(cwd, 'namelist', '.DS_Store')):
            os.unlink(os.path.join(cwd, 'namelist', '.DS_Store'))

        self.namelists = os.listdir(self.storelocation)
        # print u"現有名單：",
        # print self.namelists
        self.selectclass.clear()
        self.selectclass.addItems(self.namelists)

    def makedic(self):

        current_class = unicode(self.selectclass.currentText())
        # print u"目前所選的名單是",
        # print current_class

        if current_class == '':
            pass
        else:
            fileLocation = os.path.join(os.getcwdu(), "namelist", current_class)
            self.whichClass = dict()
            try:
                with open(fileLocation, mode='r') as infile:
                #讀取第一行，當作欄位名稱，再將其餘當作資料內容
                    self.title = infile.readline().lstrip("\n").rstrip("\n").decode('utf-8').split('\t')

                    self.content = infile.read().lstrip("\n").rstrip("\n").decode('utf-8')
                    self.content = self.content.split('\n')
                    for row in self.content:
                        row = row.split('\t')
                        self.whichClass[row[0]] = row[1]
                self.allnumber = self.whichClass.keys()
            except IOError as e:
                QMessageBox.warning(self, u"沒有這個名單喔", u"沒有這個名單喔！\n你應該是剛剛把它刪掉了\n請重新啟動程式吧~")
            except IndexError:
                QMessageBox.warning(self, u"名單格式不對喔", u"名單格式不對喔！\n記得要用tab鍵分隔姓名和學號喔\n請重新啟動程式吧~")
                os.unlink(fileLocation)

        self.spinbox.setMaximum(len(self.allnumber))
        self.spinbox.setValue(1)
        self.viewResultTable.setHorizontalHeaderLabels(self.title)


    def moreac(self):
        m = QMenu(self)
        a = m.addAction(u"匯入")
        self.connect(a, SIGNAL("triggered()"), self.add_group)
        iconim = QIcon()
        iconim.addPixmap(QPixmap("icons/import.png"), QIcon.Normal, QIcon.Off)
        a.setIcon(iconim)

        b = m.addAction(u"刪除")
        self.connect(b, SIGNAL("triggered()"), self.rem_group)
        iconde = QIcon()
        iconde.addPixmap(QPixmap("icons/delete.png"), QIcon.Normal, QIcon.Off)
        b.setIcon(iconde)
        m.exec_(QCursor.pos())

    def add_group(self):
        # print "編輯新名單"
        from openfile import opf
        #雙視窗弄了半天，原來在變數前要加 self!!
        self.ma = opf()

    def rem_group(self):
        from Delname import delf

        self.mr = delf()

    def random_choice(self, numbers):

        import random

        random.shuffle(self.allnumber)
        for i in range(numbers):

            try:
                text = self.allnumber.pop()
            except IndexError:
                QMessageBox.warning(self, u"下面沒人了", u"都抽完了！\n請重新啟動程式吧~")


            self.update_tableview(self.whichClass, text)
            self.spinbox.setMaximum(len(self.allnumber))

            if len(self.allnumber) == 0:
                QMessageBox.warning(self, u"下面沒人了", u"都抽完了！下面沒人了！\n請重新啟動程式吧~")
                break

            self.spinbox.setFocus(True)
            self.spinbox.setValue(1)

    def del_old_table(self):

        for i in reversed(range(self.row + 1)):
            self.viewResultTable.removeRow(i)

    def update_tableview(self, whichClass, text):

        schoolNumber = QTableWidgetItem(text)
        studentName = QTableWidgetItem(whichClass[text])

        self.row = self.viewResultTable.rowCount()
        self.viewResultTable.insertRow(self.row)
        self.viewResultTable.setItem(self.row, 0, schoolNumber)
        self.viewResultTable.setItem(self.row, 1, studentName)
        self.viewResultTable.item(self.row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.viewResultTable.item(self.row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()

