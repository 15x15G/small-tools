encoder1 = [
    '\\uxxxx或\\Uxxxxxxxx解码', '\\xaa\\xbb解码', '%12%34解码', '&#1234; 解码',
    'U+xxxx解码', '摩斯密码解码', 'base64解码'
]
encoder2 = [
    'UTF-8', 'windows-1252', 'GBK', 'GB18030', 'Big5', 'Shift_Jis',
    'iso-8859-1', 'latin-1'
]

import tkinter
import tkinter.ttk as ttk
from tkinter import font
from tkinter.constants import *
import urllib.parse  #转义 &#1234
import html  #转义 &#1234
import re  #转义 U+1234
import base64  # 转义base64


class App:
    def __init__(self):
        tk = tkinter.Tk()
        tk.title("编码转换工具")
        tk.geometry('500x400+100+100')
        #Misc.grid_rowconfigure(tk, 0, weight=1)
        tkinter.Misc.grid_columnconfigure(tk, 0, weight=1)
        tkinter.Misc.grid_rowconfigure(tk, 1, weight=1)
        tkinter.Misc.grid_columnconfigure(tk, 1, weight=1)

        self.listbox_encode = ttk.Combobox(tk,
                                           state="readonly",
                                           values=encoder1)
        self.listbox_encode.grid(padx=2,
                                 pady=2,
                                 row=0,
                                 column=0,
                                 sticky="NSEW")
        self.listbox_encode.current(0)
        self.listbox_encode.bind('<<ComboboxSelected>>', self.convert)

        self.listbox_decode = ttk.Combobox(tk,
                                           state="readonly",
                                           values=encoder2)
        self.listbox_decode.grid(padx=2,
                                 pady=2,
                                 row=0,
                                 column=1,
                                 sticky="NSEW")
        self.listbox_decode.bind('<<ComboboxSelected>>', self.convert)
        self.listbox_decode.current(0)

        fonts = list(font.families())
        customFont = font.Font(family='Arial')
        if ('Arial Unicode MS' in fonts):
            customFont = font.Font(family='Arial Unicode MS')
        if ('Go Noto Current' in fonts):
            customFont = font.Font(family='Go Noto Current')
        print(customFont.actual())
        self.label_encode = tkinter.Text(tk,
                                         undo=True,
                                         maxundo=-1,
                                         autoseparators=True,
                                         font=customFont,
                                         highlightthickness=2,
                                         highlightcolor='sky blue',
                                         highlightbackground='sky blue')
        self.label_encode.grid(padx=2, pady=2, row=1, column=0, sticky="NSEW")
        self.label_encode.bind('<<Modified>>', self.convert)

        self.label_decode = tkinter.Text(tk,
                                         state='disable',
                                         font=customFont,
                                         highlightthickness=2,
                                         highlightcolor='sky blue',
                                         highlightbackground='sky blue')
        self.label_decode.grid(padx=2, pady=2, row=1, column=1, sticky="NSEW")

        tk.mainloop()

    def convert(self, event):
        str1 = self.label_encode.get(1.0, END)
        #print(len(str1))
        if len(str1) <= 1:
            self.label_encode.edit_modified(False)
            return
        if (self.listbox_encode.get() == encoder1[0]):
            self.listbox_decode.configure(state='disabled')
            try:
                str2 = str1.encode()
                self.setcolor(self.label_encode, True)
            except:
                str2 = str1.encode(errors='replace')
                self.setcolor(self.label_encode, False)
            try:
                str3 = str2.decode("unicode-escape")
                self.setcolor(self.label_decode, True)
            except:
                str3 = str2.decode("unicode-escape", errors='replace')
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[1]):
            self.listbox_decode.configure(state='readonly')
            try:
                str2 = str1.encode('latin1').decode('unicode_escape')
                self.setcolor(self.label_encode, True)
            except:
                str2 = str1.encode('latin1',
                                   errors='replace').decode('unicode_escape',
                                                            errors='replace')
                self.setcolor(self.label_encode, False)
            try:
                str3 = str2.encode('latin1').decode(self.listbox_decode.get())
                self.setcolor(self.label_decode, True)
            except:
                str3 = str2.encode('latin1', errors='replace').decode(
                    self.listbox_decode.get(), errors='replace')
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[2]):
            self.listbox_decode.configure(state='disabled')
            try:
                str2 = urllib.parse.unquote(str1)
                str3 = str2
                self.setcolor(self.label_encode, True)
                self.setcolor(self.label_decode, True)
            except:
                str3 = ''
                self.setcolor(self.label_encode, False)
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[3]):
            self.listbox_decode.configure(state='disabled')
            try:
                str2 = html.unescape(str1)
                str3 = str2
                self.setcolor(self.label_encode, True)
                self.setcolor(self.label_decode, True)
            except:
                str3 = ''
                self.setcolor(self.label_encode, False)
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[4]):
            self.listbox_decode.configure(state='disabled')
            try:
                str2 = re.sub(r'\s*U\+([0-9a-fA-F]+)\s*',
                              lambda m: chr(int(m.group(1), 16)), str1)
                str3 = str2
                self.setcolor(self.label_encode, True)
                self.setcolor(self.label_decode, True)
            except:
                str3 = ''
                self.setcolor(self.label_encode, False)
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[5]):
            self.listbox_decode.configure(state='disabled')
            try:
                str2 = morsecode().decode(str1)
                str3 = str2
                self.setcolor(self.label_encode, True)
                self.setcolor(self.label_decode, True)
            except Exception as e:
                str3 = ''
                self.setcolor(self.label_encode, False)
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[6]):
            self.listbox_decode.configure(state='readonly')
            try:
                str1 = re.sub(r'[^0-9a-zA-Z+-\/_=]', '', str1)
                str1 = str1.replace('+', '-').replace('/', '_')
                while len(str1) % 4 != 0:
                    str1 += '='
                str2 = base64.urlsafe_b64decode(str1)

                str3 = str2.decode(self.listbox_decode.get())
                self.setcolor(self.label_decode, True)
            except Exception as e:
                print(str(e))
                str2 = base64.urlsafe_b64decode(str1)
                str3 = str2.decode(self.listbox_decode.get(), errors='replace')
                self.setcolor(self.label_decode, False)
        elif (self.listbox_encode.get() == encoder1[7]):
            self.listbox_decode.configure(state='disabled')
            try:
                pass
            except Exception as e:
                pass
        self.label_decode.configure(state='normal')
        self.label_decode.delete(1.0, END)
        self.label_decode.insert(1.0, str3)
        self.label_decode.configure(state='disabled')

        self.label_encode.edit_modified(False)

    def setcolor(self, wiget, bool):
        if bool:
            wiget.config(highlightcolor='green', highlightbackground='green')
        else:
            wiget.config(highlightcolor='red', highlightbackground='red')


class Tooltip:
    '''
    It creates a tooltip for a given widget as the mouse goes on it.

    see:

    http://stackoverflow.com/questions/3221956/
           what-is-the-simplest-way-to-make-tooltips-
           in-tkinter/36221216#36221216

    http://www.daniweb.com/programming/software-development/
           code/484591/a-tooltip-class-for-tkinter

    - Originally written by vegaseat on 2014.09.09.

    - Modified to include a delay time by Victor Zaccardo on 2016.03.25.

    - Modified
        - to correct extreme right and extreme bottom behavior,
        - to stay inside the screen whenever the tooltip might go out on
          the top but still the screen is higher than the tooltip,
        - to use the more flexible mouse positioning,
        - to add customizable background color, padding, waittime and
          wraplength on creation
      by Alberto Vassena on 2016.11.05.

      Tested on Ubuntu 16.04/16.10, running Python 3.5.2

    TODO: themes styles support
    '''
    def __init__(self,
                 widget,
                 *,
                 bg='#FFFFEA',
                 pad=(5, 3, 5, 3),
                 text='widget info',
                 waittime=400,
                 wraplength=250):

        self.waittime = waittime  # in miliseconds, originally 500
        self.wraplength = wraplength  # in pixels, originally 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.onEnter)
        self.widget.bind("<Leave>", self.onLeave)
        self.widget.bind("<ButtonPress>", self.onLeave)
        self.bg = bg
        self.pad = pad
        self.id = None
        self.tw = None

    def onEnter(self, event=None):
        self.schedule()

    def onLeave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def show(self):
        def tip_pos_calculator(widget,
                               label,
                               *,
                               tip_delta=(10, 5),
                               pad=(5, 3, 5, 3)):

            w = widget

            s_width, s_height = w.winfo_screenwidth(), w.winfo_screenheight()

            width, height = (pad[0] + label.winfo_reqwidth() + pad[2],
                             pad[1] + label.winfo_reqheight() + pad[3])

            mouse_x, mouse_y = w.winfo_pointerxy()

            x1, y1 = mouse_x + tip_delta[0], mouse_y + tip_delta[1]
            x2, y2 = x1 + width, y1 + height

            x_delta = x2 - s_width
            if x_delta < 0:
                x_delta = 0
            y_delta = y2 - s_height
            if y_delta < 0:
                y_delta = 0

            offscreen = (x_delta, y_delta) != (0, 0)

            if offscreen:

                if x_delta:
                    x1 = mouse_x - tip_delta[0] - width

                if y_delta:
                    y1 = mouse_y - tip_delta[1] - height

            offscreen_again = y1 < 0  # out on the top

            if offscreen_again:
                # No further checks will be done.

                # TIP:
                # A further mod might automagically augment the
                # wraplength when the tooltip is too high to be
                # kept inside the screen.
                y1 = 0

            return x1, y1

        bg = self.bg
        pad = self.pad
        widget = self.widget

        # creates a toplevel window
        self.tw = tk.Toplevel(widget)

        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)

        win = tk.Frame(self.tw, background=bg, borderwidth=0)
        label = tk.Label(win,
                         text=self.text,
                         justify=tk.LEFT,
                         background=bg,
                         relief=tk.SOLID,
                         borderwidth=0,
                         wraplength=self.wraplength)

        label.grid(padx=(pad[0], pad[2]),
                   pady=(pad[1], pad[3]),
                   sticky=tk.NSEW)
        win.grid()

        x, y = tip_pos_calculator(widget, label)

        self.tw.wm_geometry("+%d+%d" % (x, y))

    def hide(self):
        tw = self.tw
        if tw:
            tw.destroy()
        self.tw = None


class morsecode:
    def __init__(self):
        self.morse_code = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ', ': '--..--',
            '.': '.-.-.-',
            '?': '..--..',
            '/': '-..-.',
            '-': '-....-',
            '(': '-.--.',
            ')': '-.--.-',
            ' ': ' '
        }
        self.morse_code_rev = dict(
            (v, k) for (k, v) in self.morse_code.items())

    def encode(self, string):
        return ' '.join(self.morse_code[char] for char in string.upper())

    def decode(self, string):
        return ''.join(
            str(self.morse_code_rev.get(char) or '')
            for char in re.split(r'[\s\\\/]+', string))


if __name__ == '__main__':
    a = App()
