# coding: utf-8
__author__ = "João Marcos S. e Araújo"
__email__ = "marcosjoao37@hotmail.com.br"

from tkinter import messagebox
from src.funcoes.move_and_copy import MoveAndCopy
from sys import exit
import os

class Controller:
    def __init__(self):
        self.mac = MoveAndCopy()

    def workOnChoice(self, choice, directory):
        if(os.name == "posix"):
            # Unix like...
            if not directory.endswith("/"):
                directory = directory+"/"
                #os.chdir(directory)
        elif(os.name == "nt"):
            # Windows like...
            if not directory.endswith("\\"):
                directory = directory+"\\"
                #os.chdir(directory)
        else:
            messagebox.showerror("ERROR","Opss... Could not determine your OS... Exiting... :(")
            exit(0)
        try:
            if choice == "MOVE":
                self.mac.moveFiles(directory)
            elif choice == "COPY":
                self.mac.copyFiles(directory)
            else:
                messagebox.showerror("ERROR","Any choice requested!")
        except Exception as error:
            print("ERROR: "+str(error))
            messagebox.showerror("ERROR","Opss... Something went wrong... :(")
