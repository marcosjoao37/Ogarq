# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from funcoes.DicionarioDeArquivos import DicionarioDeArquivos
from funcoes.Ogarq import Ogar


class MyApp:
    def __init__(self, parent):

        self.esc = "0"

        label_width = 45

        button_width = 15
        button_width_a = 47
        button_padx = "2m"
        button_pady = "1m"

        self.myParent = parent

        self.container = Frame(parent)
        self.container.pack()

        self.labelFrame = Frame(self.container)
        self.labelFrame.pack(side=TOP)

        self.buttonsFrame = Frame(self.container)
        self.buttonsFrame.pack(side=TOP)

        self.okFrame = Frame(self.container)
        self.okFrame.pack(side=BOTTOM, expand=YES)

        # Label
        self.label1 = Label(self.labelFrame, text = "ESCOLHA UMA OPÇÃO PARA ORGANIZAÇÃO DOS ARQUIVOS")
        self.label1.configure(
            width = label_width,
            padx = button_padx,
            pady = button_pady,
        )
        self.label1.pack(side=TOP)

        self.label2 = Label(self.labelFrame, text = "UM MOVE OS ARQUIVOS, O OUTRO COPIA")
        self.label2.configure(
            width = label_width,
            padx = button_padx,
            pady = button_pady,
        )
        self.label2.pack(side=BOTTOM)

        # Botão1
        self.button1 = Button(self.buttonsFrame)
        self.button1.configure(
            width = button_width,
            padx = button_padx,
            pady = button_pady,
            text = "MOVER",
            background = "RED"
        )
        self.button1.bind("<Button-1>", lambda event, opc="1": self.buttonClicked_b(event, opc))
        self.button1.pack(side=LEFT)

        # Botão2
        self.button2 = Button(self.buttonsFrame)
        self.button2.configure(
            width = button_width,
            padx = button_padx,
            pady = button_pady,
            text = "COPIAR",
            background = "RED"
        )
        self.button2.bind("<Button-1>", lambda event, opc="2": self.buttonClicked_b(event, opc))
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
            text = "ESCOLHA O DIRETÓRIO",
            background = "BLUE"
        )
        self.buttonEntrada.bind("<Button-1>", lambda event: self.buttonEntradaDef(event))
        self.buttonEntrada.pack(side=TOP)

        # EntradaDoDiretorio
        self.entradaDir = Entry(self.okFrame, justify=CENTER)
        self.entradaDir.configure(
            width = button_width_a
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
            text = "OK",
        )
        self.button3.bind("<Button-1>", lambda event, esc=self.esc: self.buttonOk(event))
        self.button3.pack(side=BOTTOM)

    def buttonEntradaDef(self, event):
        self.entradaDir.delete(0, END)
        self.entradaDir.insert(0, filedialog.askdirectory(initialdir="/home", parent=self.myParent, mustexist=True))

    def buttonOk(self, event):
        if self.esc == "0":
            message.showerror("ERRO","ESCOLHAR COPIAR OU MOVER!")
        elif self.entradaDir.get() == '':
            message.showerror("ERRO","DIRETÓRIO INVÁLIDO")
        else:
            ogarq.leituraEsc(self.esc, self.entradaDir.get())

    def buttonClicked_b(self, event, opc):
        self.esc = opc
        if self.esc == "2":
            self.button1["background"] = "red"
            self.button2["background"] = "green"
        elif self.esc == "1":
            self.button1["background"] = "green"
            self.button2["background"] = "red"
        print(self.esc)

message = messagebox
dda = DicionarioDeArquivos()
ogarq = Ogar()