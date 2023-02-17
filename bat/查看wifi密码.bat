@echo off
chcp 65001
netsh wlan show profiles
set /p id=SSID: 
netsh wlan show  profile name=%id% key=clear
pause
