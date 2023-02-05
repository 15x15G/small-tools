;@Findstr -bv ;@F "%~f0" | powershell -command - & Pause & goto:eof

try {
    $result = Get-WinEvent -MaxEvents 1 -ErrorAction Stop -FilterHashtable @{LogName = 'System'; Id = 225; StartTime=(Get-Date).AddDays(-1) }
}

catch [Exception] {
        Write-Host $_.Exception;
        Exit
}

$eventXml = ([xml]$result.ToXml()).Event

$eventData = $eventXml.EventData.Data

$CommandLine = ($eventData | Where-Object { $_.Name -eq 'CommandLine' }).'#text'

Write-Output $CommandLine

