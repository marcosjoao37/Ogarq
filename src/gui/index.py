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
        self.controller = Controller()
        self.fonte = ("Verdana", "16", "bold")

        # Menu bar
        self.menubar = Menu(self.parent)
        # Pulldown menu FILE
        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command(label='Select Directory', command=self.menu_file_select)
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.parent.destroy)
        self.menubar.add_cascade(label='File', menu=self.file)
        # Pulldown menu EDIT
        self.config = Menu(self.menubar, tearoff=0)
        self.config.add_command(label='Settings', command=self.menu_edit_settings)
        self.menubar.add_cascade(label='Edit', menu=self.config)
        # Pulldown menu HELP
        self.help = Menu(self.menubar, tearoff=0)
        self.help.add_command(label='About', command=self.menu_help_about)
        self.menubar.add_cascade(label='Help', menu=self.help)
        # Display the menu bar
        self.parent.config(menu=self.menubar)
        

        Label(self.parent, text="Organize your files!", font=self.fonte).grid(row=1, column=1, columnspan=2,
                                                                         stick=E+W, pady=5, padx=10)
        Label(self.parent, text="Directory:").grid(row=2, column=1,
                                                   stick=E+W, pady=3)
        self.input_dir = Entry(self.parent)
        self.input_dir.grid(row=2, column=2, stick=E+W, pady=3)

        self.choice_dir_button = Button(self.parent, command=self.choice_dir,
                                        text="Select Directory")
        self.choice_dir_button.grid(row=3, column=2, stick=E+W, pady=3)

        self.status_label = Label(self.parent, text="Waiting...", font=("Verdana", "12", "bold"))
        self.status_label['height'] = 3
        self.status_label.grid(row=4, column=1, columnspan=2, stick=E+W, pady=3)

        self.organize_button = Button(self.parent, command=self.organize,
                                      text="ORGANIZE!")
        self.organize_button.grid(row=5, column=1, columnspan=2, pady=3)

    def choice_dir(self):
        self.status_label['text'] = "Waiting..."
        self.input_dir.delete(0, END)
        self.input_dir.insert(0, filedialog.askdirectory(
            initialdir="~", parent=self.parent, mustexist=True))

    def organize(self):
        if (self.input_dir.get() == ""):
            messagebox.showinfo("INFORMATION","Invalide directory!")
        else:
            self.status_label['text'] = "Organizing..."
            self.controller.workOnChoice("MOVE", self.input_dir.get())
            self.status_label['text'] = "DONE!"

    def menu_edit_settings(self):
        settings_parent = Tk()
        settings_parent.resizable(width=False, height=False)
        settings_parent.title('Settings')
        settings_parent.eval("tk::PlaceWindow %s center" % settings_parent.winfo_pathname(settings_parent.winfo_id()))
        Settings(settings_parent)

    def menu_help_about(self):
        about_parent = Tk()
        about_parent.resizable(width=False, height=False)
        about_parent.title('About')
        about_parent.eval("tk::PlaceWindow %s center" % about_parent.winfo_pathname(about_parent.winfo_id()))
        About(about_parent)

    def menu_file_select(self):
        self.choice_dir()
