@echo off 
rmdir build /s /q
pause
setup_cxfreeze.py build

@echo ���U�ӭn���Y�üƵ{��
pause

"C:\Program Files\7-Zip\7z.exe" a -tzip build\����-�ۭq�W��.zip build\exe.win32-2.7
@echo ���U�ӭn�s�@�w���ɮ�

@echo
rem "C:\Program Files (x86)\Inno Setup 5\Compil32.exe" /cc "C:\Users\Aaron\Documents\random_choice_portable_Ramdisk.iss"

@echo
@echo ���U�ӭn�s�u�� ftp
pause

"C:\Program Files (x86)\FileZilla FTP Client\filezilla.exe" --site="0D99 manager"