Get-ChildItem -Path "C:\Windows\", "c:\", "$env:USERPROFILE" -Force |
Where-Object { $_.LinkType -ne $null -or $_.Attributes -match "ReparsePoint" } |
Format-Table FullName, Length, Attributes, Linktype, Target
