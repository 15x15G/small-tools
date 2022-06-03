
if WScript.Arguments.Count = 0 then
    WScript.Echo "Missing parameters"
    WScript.Quit 1
end if

filepath ="""" & WScript.Arguments(0) & """"

' If running under wscript.exe, relaunch under cscript.exe in a hidden window...
If InStr(1, WScript.FullName, "wscript.exe", vbTextCompare) > 0 Then
    With CreateObject("WScript.Shell")
        WScript.Quit .Run("cscript.exe """ & WScript.ScriptFullName & """ " & filepath, 0, True)
    End With
End If

' "Real" start of script. We can run Exec() hidden now...
Dim strOutput
strOutput = CreateObject("WScript.Shell").Exec("certutil -hashfile " & filepath & " MD5").StdOut.ReadAll()

' Need to use MsgBox() since WScript.Echo() is sent to hidden console window...
MsgBox strOutput, vbOKOnly + vbInformation + vbDefaultButton1 + vbSystemModal, "Hash"
