@echo off 
SETLOCAL EnableDelayedExpansion
chcp 65001
cls
set "exe=C:\Program Files\7-Zip\7z"
set "pwlist=password.txt"
for %%i in (%*) do (
    echo [1m%%i[0m
    call :inner %%i  
)
goto :eof


:inner
    SET /A n = 0
    cd /d %~dp1
    for /F "usebackq tokens=*" %%A in ("%pwlist%") do (
        "%exe%" l %1 -sccUTF-8 "-p%%A" >nul 2>nul && (
        echo [42m [OK:list] %%A [0m
        "%exe%g" x  %1 -aou -sccUTF-8 "-p%%A" -o%~dp1 >nul 2>nul && (
	echo [42m [OK:unzip] %%A [0m
	goto :break
	)
        ) || (
        echo [41m [NG:unzip] %%A [0m
        SET /a n+=1
        )
    )
    echo [41m [password no find. tried %n% times.] [0m
    pause
    :break
    timeout 1 >nul
    goto :eof
