@echo off
chcp 65001
netsh wlan show  profile name="此处填入SSID" key=clear
pause