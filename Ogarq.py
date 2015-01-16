# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'
# Organizador em pastas de acordo com os seus respectivos tipos.
# .jpg, .png, .bmp para a pasta fotos; .flv, .wmv, .mp4 para a pasta vídeos e etc.

from tkinter import messagebox
import sys, shutil, glob, os

class Ogar:
    def __init__(self):
        pass

    def leituraArq(self, esc, dir):

        self.procDir(dir)

        self.criarPastas()

        os.system("sudo chmod -R 777 "+self.dir)

        self.listFoto = [glob.glob(self.dir+"*.jpg"), glob.glob(self.dir+"*.png"), glob.glob(self.dir+"*.bmp"), glob.glob(self.dir+"*.jpeg"), glob.glob(self.dir+"*.gif")]
        self.listVid = [glob.glob(self.dir+"*.wmv"), glob.glob(self.dir+"*.mp4"), glob.glob(self.dir+"*.mkv"), glob.glob(self.dir+"*.rmvb"), glob.glob(self.dir+"*.flv"), glob.glob(self.dir+"*.3gp"), glob.glob(self.dir+"*.avi"), glob.glob(self.dir+"*.mov")]
        self.listMus = [glob.glob(self.dir+"*.mp3"), glob.glob(self.dir+"*.wav"), glob.glob(self.dir+"*.flac"), glob.glob(self.dir+"*.aac")]
        self.listScr = [glob.glob(self.dir+"*.bbbsh"), glob.glob(self.dir+"*.aaapy"), glob.glob(self.dir+"*.java"), glob.glob(self.dir+"*.bat")]
        self.listDoc = [glob.glob(self.dir+"*.doc"), glob.glob(self.dir+"*.docx"), glob.glob(self.dir+"*.txt"), glob.glob(self.dir+"*.odt")]

        print("após as listas.")
        print(self.listFoto)
        print(esc)

        try:
            print("após o Try.")
            if esc == "1":
                print("1")
                self.moverArq()
            elif esc == "2":
                print("2")
                self.copiarArq()

            os.system("sudo chmod -R 777 "+self.dir)

            messagebox.showinfo("INFORMAÇÃO","TUDO PRONTO E ORGANIZADO!")
        except:
            messagebox.showinfo("INFORMAÇÃO","OPSS... ALGO DEU ERRADO.")

    def criarPastas(self):
        if ("Scripts") not in os.listdir("."):
            os.mkdir(self.dir+"Fotos"), os.mkdir(self.dir+"Vídeos"), os.mkdir(self.dir+"Documentos"), os.mkdir(self.dir+"Músicas"), os.mkdir(self.dir+"Scripts")

        else:
            print("Pastas já existentes.")

    def moverArq(self):
        try:
            print(self.listFoto)
            for lista in self.listFoto:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    print(arq)
                    os.chdir(self.dir+"Fotos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Fotos")

            for lista in self.listVid:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Vídeos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Vídeos")

            for lista in self.listMus:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Músicas")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Músicas")

            for lista in self.listDoc:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Documentos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Documentos")

            for lista in self.listScr:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Scripts")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Scripts")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def copiarArq(self):
        try:
            for lista in self.listFoto:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Fotos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Fotos")

            for lista in self.listVid:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Vídeos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Vídeos")

            for lista in self.listMus:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Músicas")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Músicas")

            for lista in self.listDoc:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Documentos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Documentos")

            for lista in self.listScr:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Scripts")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Scripts")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def procDir(self, dir):
        if os.path.isdir(dir):
            self.dir = dir
            messagebox.showinfo("INFORMAÇÃO","DIRETÓRIO ENCONTRADO!")
            return True
        else:
            messagebox.showinfo("INFORMAÇÃO","OPSS... DIRETÓRIO NÃO ENCONTRADO!")
            return False


shutill = shutil
message = messagebox
