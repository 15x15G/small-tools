powershell (Add-Type -MemberDefinition '[DllImport(\"user32.dll\")]^public static extern void LockWorkStation();' -Name WinAPI -Namespace Extern -PassThru)::LockWorkStation()

