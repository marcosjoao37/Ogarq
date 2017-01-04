# coding: utf-8
__author__ = "João Marcos S. e Araújo"
__email__ = "marcosjoao37@hotmail.com.br"

"""
Author: João Marcos Silva e Araújo
Project: https://github.com/marcosjoao37/Ogarq
Facebook: https://www.facebook.com/marcosjoao38
E-mail: marcosjoao37@hotmail.com.br
"""

from tkinter import *
from src.gui.index import Index
import os


parent = Tk()

parent.resizable(width=False, height=False)
icon = PhotoImage(file="src/icon.png")
parent.tk.call('wm', 'iconphoto', parent._w, icon)
parent.title('Ogarq')
parent.eval("tk::PlaceWindow %s center" % parent.winfo_pathname(parent.winfo_id()))

Index(parent)
parent.mainloop()
