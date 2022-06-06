@echo off

set a=%~n0

powershell -NoProfile -Command "& {$string = (Get-FileHash $args[1] -Algorithm $args[0]).hash; Add-Type -AssemblyName PresentationFramework;$UserResponse=[System.Windows.MessageBox]::Show(\"$string`n`nClick OK to copy to clipboard\", $args, 1);if($UserResponse -eq \"OK\"){Set-Clipboard -Value $string}}" "%a%" """%1""" 
