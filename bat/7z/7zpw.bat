@echo off 
SETLOCAL EnableDelayedExpansion
chcp 65001
cls
set "exe=C:\Program Files\7-Zip\7z.exe"
set "pwlist=D:\新建文件夹\Github\small-tools\bat\7z\password.txt"
for %%i in (%*) do (
    echo [1m%%i[0m
    call :inner %%i  
)
pause
goto :eof


:inner
    SET /A n = 0
    cd /d %~dp1
    for /F "usebackq tokens=*" %%A in ("%pwlist%") do (
        "%exe%" t %1 -sccUTF-8 "-p%%A" >nul 2>nul && (
        echo [42m [OK] %%A [0m
        "%exe%" x  %1 -aou -sccUTF-8 "-p%%A" -o*~  >nul
        goto :break
        ) || (
        SET /a n+=1
        )
    )
    echo [41m [password no find. tried %n% times.] [0m
    :break
    goto :eof
