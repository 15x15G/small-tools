@echo off
chcp 65001
set /p id=SSID: 
netsh wlan show  profile name=%id% key=clear
pause