@echo off 
chcp 65001
SETLOCAL EnableDelayedExpansion
cls
for %%i in (%*) do (
    echo [1m%%i[0m
    call :inner %%i  
)
pause
goto :eof


:inner
    SET /A n = 0
    for /F "usebackq tokens=*" %%A in ("password.txt") do (
        "C:\Program Files\7-Zip\7z.exe" t %1 -sccUTF-8 "-p%%A" >nul 2>nul && (
        echo [42m [OK] %%A [0m
        start /b "" "C:\Program Files\7-Zip\7z.exe" x  %1 -aou -sccUTF-8 "-p%%A" -o*~  >nul
        goto :break
        ) || (
        SET /a n+=1
        )
    )
    echo [41m [password no find. tried %n% times.] [0m
    :break
    goto :eof
