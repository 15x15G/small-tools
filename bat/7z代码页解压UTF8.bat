echo 代码页列表：https://zh.wikipedia.org/wiki/代码页
for %%i in (%*) do (
start /b "" "C:\Program Files\7-Zip\7z.exe" x  %%i -mcp=65001  -o*
)
pause