echo off
rem 关闭自动输出
setlocal ENABLEDELAYEDEXPANSION
mode con: cols=65 lines=25
color 0a
rem 批处理获取管理员权限
:-------------------------------------  
%1 mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&&exit /b
CD /D "%~dp0"
:-------------------------------------  


:begin

rem 接收输入

set name=
set Fpath=
set /p name=请输入防火墙策略名称(使用软件名即可):
set /p Fpath=请输入软件安装路径(C:\Program Files\WinRAR):

rem 输出得到的输入信息
echo 您输入的防火墙策略名称是：%name%
echo 您输入的软件安装路径是：%Fpath%


echo "确认请按任意键否则请按Ctrl+C取消"
pause

setlocal enabledelayedexpansion
set /a n=0
for /r "%Fpath%" %%i in (*.exe) do (
    set /a n+=1
    echo "!n!_%name%","%%i" 
    netsh advfirewall firewall del rule name="!n!_%name%">nul 2>nul
    netsh advfirewall firewall add rule name="!n!_%name%" program="%%i" action=block dir=out>null
    echo 阻止!n!_%name%程序出站规则已添加成功
)

rem pause>null

echo.

rem 从begin标签出，再次运行
goto begin
