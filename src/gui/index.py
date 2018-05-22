# coding: utf-8
__author__ = "João Marcos S. e Araújo"
__email__ = "marcosjoao37@hotmail.com.br"

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from src.gui.about import About
from src.gui.settings import Settings
from src.funcoes.controller import Controller


class Index:
    def __init__(self, parent):
        self.parent = parent
        self.fonte = ("Verdana", "16", "bold")

        # Menu bar
        self.menubar = Menu(self.parent)
        # Pulldown menu FILE
        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command(label='Select Directory',
                              command=self.menu_file_select)
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.parent.destroy)
        self.menubar.add_cascade(label='File', menu=self.file)
        # Pulldown menu EDIT
        self.config = Menu(self.menubar, tearoff=0)
        self.config.add_command(
            label='Settings', command=self.menu_edit_settings)
        self.menubar.add_cascade(label='Edit', menu=self.config)
        # Pulldown menu HELP
        self.help = Menu(self.menubar, tearoff=0)
        self.help.add_command(label='About', command=self.menu_help_about)
        self.menubar.add_cascade(label='Help', menu=self.help)
        # Display the menu bar
        self.parent.config(menu=self.menubar)

        # Body
        Label(self.parent, text="Organize your files!", font=self.fonte).grid(
            row=1, column=1, columnspan=2, stick=E + W, pady=5, padx=10)

        Label(self.parent, text="Directory:").grid(row=2, column=1,
                                                   stick=W, pady=3, padx=(10, 0))
        self.input_dir = Entry(self.parent)
        self.input_dir.grid(row=2, column=2, stick=E, pady=3, padx=(0, 10))

        self.choice_dir_button = Button(self.parent, command=self.choice_dir,
                                        text="Select directory")
        self.choice_dir_button.grid(
            row=3, column=1, columnspan=2, stick=E + W, pady=3, padx=10)

        self.status_label = Label(
            self.parent, text="First, select a directory", font=("Verdana", "10", "bold"))
        self.status_label['height'] = 3
        self.status_label.grid(
            row=4, column=1, columnspan=2, stick=E + W, pady=3)

        self.organize_button = Button(self.parent, command=self.organize,
                                      text="Start!", state=DISABLED)
        self.organize_button.grid(
            row=5, column=1, columnspan=2, pady=5, stick=E, padx=(0, 10))

    def choice_dir(self):
        selected_dir = filedialog.askdirectory(
            initialdir="~", parent=self.parent, mustexist=True)
        self.input_dir.delete(0, END)
        self.input_dir.insert(0, selected_dir)

        if(len(selected_dir) > 0):
            self.organize_button.config(state=NORMAL)
            self.status_label['text'] = "Now, start organizing!"

    def organize(self):
        if (self.input_dir.get() == ""):
            messagebox.showinfo("INFORMATION", "Invalide directory!")
        else:
            self.status_label['text'] = "Organizing..."
            self.controller = Controller()
            self.controller.workOnChoice("MOVE", self.input_dir.get())
            self.status_label['text'] = "Done!"

    def menu_edit_settings(self):
        Settings(self.parent)

    def menu_help_about(self):
        About(self.parent)

    def menu_file_select(self):
        self.choice_dir()
