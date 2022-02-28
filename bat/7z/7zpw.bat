@echo off 
chcp 65001
SETLOCAL EnableDelayedExpansion

for %%i in (%*) do (
    echo %%i
    call :inner %%i  
)
pause
goto :eof


:inner
    for /F "usebackq tokens=*" %%A in ("password.txt") do (
        "C:\Program Files\7-Zip\7z.exe" t %1 -sccUTF-8 "-p%%A" >nul 2>nul && (
        echo [OK] %%A 
        start /b "" "C:\Program Files\7-Zip\7z.exe" x  %1 -aou -sccUTF-8 "-p%%A" -o*~
        goto :break
        ) || (
        echo [error] %%A 
        )
    )
    echo [password no find]
    :break
    goto :eof
