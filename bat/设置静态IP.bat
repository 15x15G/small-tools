@echo off

:-------------------------------------  
%1 mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&&exit /b
CD /D "%~dp0"
:-------------------------------------  

chcp 65001
netsh interface ipv4 set address name="以太网" static 192.168.0.31 255.255.255.0
pause