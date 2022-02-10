import win32con, win32api

win32api.PostMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND,
                     win32con.SC_MONITORPOWER, 2)
