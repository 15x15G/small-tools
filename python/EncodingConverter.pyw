encoder = [
    'UTF-8', 'windows-1252', 'GBK', 'GB18030', 'Big5', 'Shift_Jis',
    'iso-8859-1'
]
# str = '娴嬭瘯'

# for de in encoder:
#     for en in encoder:
#         if en!=de :
#             print(f'{en} -> {de}:\t\t',
#                   str.encode(en, errors='ignore').decode(de, errors='ignore'))

import tkinter
import tkinter.ttk as ttk
from tkinter.constants import *


def convert(event):
    str1 = label_encode.get(1.0, END)
    if len(str1)==0: return
    str2 = str1.encode(listbox_encode.get(), errors='ignore')
    str3 = str2.decode(listbox_decode.get(), errors='ignore')

    label_decode.configure(state='normal')
    label_decode.delete(1.0, END)
    label_decode.insert(1.0, str3)
    label_decode.configure(state='disabled')

    label_encode.edit_modified(False)


tk = tkinter.Tk()
tk.title("乱码转换工具")
tk.geometry('500x400+100+100')
#Misc.grid_rowconfigure(tk, 0, weight=1)
tkinter.Misc.grid_columnconfigure(tk, 0, weight=1)
tkinter.Misc.grid_rowconfigure(tk, 1, weight=1)
tkinter.Misc.grid_columnconfigure(tk, 1, weight=1)

listbox_encode = ttk.Combobox(tk, state="readonly", values=encoder)
listbox_encode.grid(padx=2, pady=2, row=0, column=0, sticky="NSEW")
listbox_encode.current(2)
listbox_encode.bind('<<ComboboxSelected>>', convert)


listbox_decode = ttk.Combobox(tk, state="readonly", values=encoder)
listbox_decode.grid(padx=2, pady=2, row=0, column=1, sticky="NSEW")
listbox_decode.bind('<<ComboboxSelected>>', convert)
listbox_decode.current(0)

label_encode = tkinter.Text(tk)
label_encode.grid(padx=2, pady=2, row=1, column=0, sticky="NSEW")
label_encode.bind('<<Modified>>', convert)

label_decode = tkinter.Text(tk,state='disable')
label_decode.grid(padx=2, pady=2, row=1, column=1, sticky="NSEW")

tk.mainloop()
