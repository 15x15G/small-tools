@echo off
set folder="D:\Documents\Tencent Files\123456789\Image\Group2" 
cd /d %folder% && (
echo deleting...
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
echo finish
) || (
echo path error
)

pause
