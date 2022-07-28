@echo off

:-------------------------------------  
%1 mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&&exit /b
CD /D "%~dp0"
:-------------------------------------  

sc config "wuauserv" start= disabled
sc stop "wuauserv"
pause