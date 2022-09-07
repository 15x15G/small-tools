@echo off
if defined EnableTouchPad (
    if %EnableTouchPad%==1 (
        %windir%\System32\SystemSettingsAdminFlows.exe EnableTouchPad 0
        setx EnableTouchPad 0 >nul
        echo DisableTouchPad
    ) else (
        %windir%\System32\SystemSettingsAdminFlows.exe EnableTouchPad 1
        setx EnableTouchPad 1 >nul
        echo EnableTouchPad
    )
) else (
    setx EnableTouchPad 0 >nul
    %windir%\System32\SystemSettingsAdminFlows.exe EnableTouchPad 0
    echo defined EnableTouchPad
    echo DisableTouchPad
)


pause
