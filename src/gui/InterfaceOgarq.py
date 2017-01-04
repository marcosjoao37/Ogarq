# coding: utf-8
__author__ = "João Marcos S. e Araújo"
__email__ = "marcosjoao37@hotmail.com.br"

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from threading import Thread
import tkinter.ttk as ttk
import time

from funcoes.Ogarq import Ogar

#Cor padrão do sistema para Ubuntu
defaultColor = "#d9d9d9"

Ogarq = Ogar()

class MyApp:
    def __init__(self, parent):

        #self.choice: move = 1, copy = 2, none = 0
        self.choice = "0"

        label_width = 45

        button_width = 15
        button_padx = "2m"
        button_pady = "1m"

        entry_width = 47
        progress_width = 150

        self.myParent = parent

        self.container = Frame(parent)
        self.container.pack()

        self.labelFrame = Frame(self.container)
        self.labelFrame.pack(side=TOP)

        self.buttonsFrame = Frame(self.container)
        self.buttonsFrame.pack(side=TOP)

        self.okFrame = Frame(self.container)
        self.okFrame.pack(side=TOP)

        # Label
        self.label1 = Label(self.labelFrame, text = "Choose one of the options below to organize your files")
        self.label1.configure(
            width = label_width,
            padx = button_padx,
            pady = button_pady,
        )
        self.label1.pack(side=TOP)

        # Botão1
        self.button1 = Button(self.buttonsFrame)
        self.button1.configure(
            width = button_width,
            padx = button_padx,
            pady = button_pady,
            text = "Move",
            background = defaultColor,
            activebackground = "sea green"
        )
        self.button1.bind("<Button-1>", lambda event, choice="1": self.buttonClicked_move(event, choice))
        self.button1.pack(side=LEFT)

        # Botão2
        self.button2 = Button(self.buttonsFrame)
        self.button2.configure(
            width = button_width,
            padx = button_padx,
            pady = button_pady,
            text = "Copy",
            background = defaultColor,
            activebackground = "sea green"
        )
        self.button2.bind("<Button-1>", lambda event, choice="2": self.buttonClicked_copy(event, choice))
        self.button2.pack(side=RIGHT)

        # LabelSeparador1
        self.labelSeparador1 = Label(self.okFrame, text = "\n")
        self.labelSeparador1.configure(
            width = label_width,
        )
        self.labelSeparador1.pack(side=TOP)

        # BotaoEntradaDoDiretorio
        self.buttonEntrada = Button(self.okFrame)
        self.buttonEntrada.configure(
            width = label_width,
            padx = button_padx,
            pady = button_pady,
            text = "Escolher diretório",
            background = defaultColor,
            activebackground = "sea green"
        )
        self.buttonEntrada.bind("<Button-1>", lambda event: self.buttonEntradaDef(event))
        self.buttonEntrada.pack(side=TOP)

        # EntradaDoDiretorio
        self.entradaDir = Entry(self.okFrame, justify=CENTER)
        self.entradaDir.configure(
            width = entry_width
        )
        self.entradaDir.pack(side=TOP)

        # LabelSeparador2
        self.labelSeparador2 = Label(self.okFrame, text = "\n")
        self.labelSeparador2.configure(
            width = label_width
        )
        self.labelSeparador2.pack(side=TOP)

        # Botão3
        self.button3 = Button(self.okFrame)
        self.button3.configure(
            width = button_width,
            padx = button_padx,
            text = "Organizar!",
            background = defaultColor,
            activebackground = "sea green"
        )
        self.button3.bind("<Button-1>", lambda event, choice=self.choice: self.buttonOk(event))
        self.button3.pack(side=TOP)

        # LabelSeparador3
        self.labelSeparador3 = Label(self.okFrame, text = "\n")
        self.labelSeparador3.configure(
            width = label_width
        )
        self.labelSeparador3.pack(side=TOP)

        # Estes elementos abaixo estão invisíveis! Eles apenas aparecerão quando o usuário apertar o botão "OK"
        # Label4
        self.label4 = Label(self.okFrame, text = "Tarefa em andamento...")
        self.label4.configure(
            width = label_width
        )
        #self.label4.pack(side=BOTTOM)

        # Barra de Progresso
        self.barraProgress = ttk.Progressbar(self.okFrame, length=progress_width, orient="horizontal", mode="indeterminate")
        #self.barraProgress.pack(side=BOTTOM)

    def buttonEntradaDef(self, event):
        self.entradaDir.delete(0, END)
        self.entradaDir.insert(0, filedialog.askdirectory(initialdir="~", parent=self.myParent, mustexist=True))

    def buttonOk(self, event):
        if self.choice == "0":
            messagebox.showinfo("INFORMATION","Choose MOVE or COPY!")
        elif self.entradaDir.get() == '':
            messagebox.showinfo("INFORMATION","Invalide directory!")
        else:
            # Widgets que estavam invisíveis aparecem
            # Aqui está tendo um problema, no qual a barra do progressbar não se move.
            # Se alguém puder me ajudar, ficaria grato :)
            self.label4.pack(side=BOTTOM, expand=True, fill=X)
            self.barraProgress.pack(side=BOTTOM, expand=True, fill=X)
            self.barraProgress.start()
            self.myParent.update()
            # Inicia as tarefas
            Ogarq.workOnChoice(self.choice, self.entradaDir.get())
            # Deixa novamente invisível a barra de progresso e muda o nome da label4 para "Tarefa concluída!"
            self.barraProgress.stop()
            self.barraProgress.pack_forget()
            self.label4.configure(text="Tarefa concluída!")

    def buttonClicked_move(self,event,choice):
        if(self.button1["background"] == defaultColor):
            self.choice = choice
            self.button1["background"] = "green"
            self.button2["background"] = defaultColor
        elif(self.button1["background"] == "green"):
            self.choice = "0"
            self.button1["background"] = defaultColor
            self.button2["background"] = defaultColor

    def buttonClicked_copy(self,event,choice):
        if(self.button2["background"] == defaultColor):
            self.choice = choice
            self.button1["background"] = defaultColor
            self.button2["background"] = "green"
        elif(self.button2["background"] == "green"):
            self.choice = "0"
            self.button1["background"] = defaultColor
            self.button2["background"] = defaultColor