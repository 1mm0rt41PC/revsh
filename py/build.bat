C:\Python38\x64\python.exe -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
C:\Python38\x86\python.exe -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz

C:\Python38\x64\Scripts\pyinstaller.exe --onefile --noconsole r.py && move /Y dist\r.exe .\r_x64.exe && rmdir /q /s build\ dist\ __pycache__\ && del /q /s r.spec 
C:\Python38\x86\Scripts\pyinstaller.exe --onefile --noconsole r.py && move /Y dist\r.exe .\r_x86.exe && rmdir /q /s build\ dist\ __pycache__\ && del /q /s r.spec
