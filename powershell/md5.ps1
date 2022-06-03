
$filepath = $args[0]
$string = (Get-FileHash $filepath -Algorithm MD5 | Format-List | Out-String).Trim()

Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show($string, "Hash", 0)

