[void][System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
[System.Windows.Forms.Application]::EnableVisualStyles()
 
$TranscodedImageCache=(Get-ItemProperty 'HKCU:\Control Panel\Desktop' TranscodedImageCache -ErrorAction Stop).TranscodedImageCache
 
$Path_Start_Delta = 24
$Path_End_Delta   = $TranscodedImageCache.length-1
for ($i = $Path_Start_Delta; $i -lt ($TranscodedImageCache.length); $i += 2)
{
    if ($TranscodedImageCache[($i+2)..($i+3)] -eq 0) {
        $Path_End_Delta=$i + 1;
        Break;
    }
}
$UnicodeObject=New-Object System.Text.UnicodeEncoding
$WallpaperSource=$UnicodeObject.GetString($TranscodedImageCache[$Path_Start_Delta..$Path_End_Delta]);
 
$result=[System.Windows.Forms.MessageBox]::Show("Wallpaper location: `r$WallpaperSource`r`rLaunch Explorer?", "Script", "YesNo", "Asterisk");
if ($result -eq "Yes")
{
    Start-Process explorer.exe -ArgumentList "/select,`"$WallpaperSource`""
}