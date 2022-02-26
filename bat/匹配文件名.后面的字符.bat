@echo off
set "Var=%~n0"
call :LoopLastToken "%Var%"
echo "%Var%"
pause
exit

:LoopLastToken
    set "Var=%~1"
    if not "%Var:*.=%"=="%~1" (
    call :LoopLastToken "%Var:*.=%")
exit /b