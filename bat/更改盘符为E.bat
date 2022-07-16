@echo off

:-------------------------------------  
%1 mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&&exit /b
CD /D "%~dp0"
:-------------------------------------  


@echo off
set DRIVERAW=%~dp0
set DRIVE=%DRIVERAW:~0,1%
set TARGET=E

echo "%DRIVE% -> %TARGET%"
if %DRIVE%==%TARGET% (exit)
for /f "tokens=2,3" %%a in ('echo list volume ^| diskpart') do (
    if %%b==%DRIVE% set VOLNO=%%a
)
del %DRIVERAW%\diskpart.txt
echo select volume %VOLNO% > %DRIVERAW%\diskpart.txt
echo assign letter=%TARGET% >> %DRIVERAW%\diskpart.txt
echo ^G
diskpart /s %DRIVERAW%\diskpart.txt
exit
