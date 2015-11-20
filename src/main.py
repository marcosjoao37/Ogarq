# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'

"""
Autor: João Marcos Silva e Araújo
Link do projeto: https://github.com/marcosjoao37/Ogarq
Meu Facebook: https://www.facebook.com/marcosjoao38
E-mail: marcosjoao37@hotmail.com.br
"""

from tkinter import *
from gui.InterfaceOgarq import MyApp
import os

root = Tk()
myapp = MyApp(root)



#Imagem do ícone
img = PhotoImage(file="src/icon.png")

#Título da janela
root.title("Ogarq")

# Carregar ícone do programa
root.tk.call('wm', 'iconphoto', root._w, img)

#centralizar tela
appW = 500
appH = 290
w = (root.winfo_screenwidth()/2) - (appW/2)
h = (root.winfo_screenheight()/2) - (appH/2)

# Dimensões da janela principal
root.geometry("%dx%d+%d+%d" % (appW, appH, w, h))

# Não permite que a janela redimensione
root.resizable(0,0)

root.mainloop()