#-*- coding: utf-8-*-
__author__ = 'Aaron'
import sys

from cx_Freeze import setup, Executable


if sys.platform == "win32":
    base = "Win32GUI"

#因為已經包含下列檔案了，所以就comment掉了
#includefiles=  ['qt.conf','del.ui', 'delf.py', 'Delname.py', 'Flaticon_1430.png', 'icons', 'icons.qrc', 'namelist', 'openfile-bak.py', 'openfile.py', 'opf.py', 'opf.ui', 'Random_choice_portable_Mac.py', 'Random_choice_portable_Mac.pyw', 'README.md', 'scales.icns','icons/delete.png', 'icons/dice.png', 'icons/eraser.png', 'icons/fdelete.png', 'icons/gear.png', 'icons/import.png', 'icons/open.png','namelist/99']
includefiles = ['qt.conf', 'delf.pyc', 'Delname.pyc', 'icons', 'namelist',
                'openfile.pyc', 'opf.pyc', 'scales.icns', ]
#記得要加上C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats 這個資料夾
includes = ['sip', 'PyQt4.QtCore']

setup(
    name="Random_Choice_CustomName",
    version="1.0",
    description=u"自訂名單亂數抽籤程式",
    options={'build_exe': {'include_files': includefiles}},
    executables=[Executable("Random_choice_portable_Mac.pyw", base=base, icon="Flaticon_1430.ico")])