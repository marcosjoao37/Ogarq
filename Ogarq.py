# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'
# Organizador em pastas de acordo com os seus respectivos tipos.
# .jpg, .png, .bmp para a pasta fotos; .flv, .wmv, .mp4 para a pasta vídeos e etc.

from tkinter import messagebox
import sys, shutil, glob, os

class Ogar:
    def __init__(self):
        pass

    def leituraArq(self, esc):

        esco = esc

        self.criarPastas()

        self.dir=str(sys.path[0])

        #os.system("sudo chmod -R 777 "+self.dir)

        self.listFoto = [glob.glob("*.jpg"), glob.glob("*.png"), glob.glob("*.bmp"), glob.glob("*.jpeg"), glob.glob("*.gif")]
        self.listVid = [glob.glob("*.wmv"), glob.glob("*.mp4"), glob.glob("*.mkv"), glob.glob("*.rmvb"), glob.glob("*.flv"), glob.glob("*.3gp"), glob.glob("*.avi"), glob.glob("*.mov")]
        self.listMus = [glob.glob("*.mp3"), glob.glob("*.wav"), glob.glob("*.flac"), glob.glob("*.aac")]
        self.listScr = [glob.glob("*.bbbsh"), glob.glob("*.aaapy"), glob.glob("*.java"), glob.glob("*.bat")]
        self.listDoc = [glob.glob("*.doc"), glob.glob("*.docx"), glob.glob("*.txt"), glob.glob("*.odt")]

        print("após as listas.")
        str(esco)
        print(esco)
        try:
            print("após o Try.")
            if esco == "1":
                print("1")
                self.moverArq()
            elif esco == "2":
                print("2")
                self.copiarArq()

            os.system("sudo chmod -R 777 "+self.dir)

            messagebox.showinfo("INFORMAÇÃO","TUDO PRONTO E ORGANIZADO!")
        except:
            messagebox.showinfo("INFORMAÇÃO","OPSS... ALGO DEU ERRADO.")

    def criarPastas(self):
        if ("Scripts") not in os.listdir("."):
            os.mkdir("Fotos"), os.mkdir("Vídeos"), os.mkdir("Documentos"), os.mkdir("Músicas"), os.mkdir("Scripts")

        else:
            print("Pastas já existentes.")

    def moverArq(self):
        try:
            print(self.listFoto)
            for lista in self.listFoto:
                for arq in lista:
                    os.chdir("Fotos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"/Fotos")

            for lista in self.listVid:
                for arq in lista:
                    os.chdir("Vídeos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"/Vídeos")

            for lista in self.listMus:
                for arq in lista:
                    os.chdir("Músicas")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"/Músicas")

            for lista in self.listDoc:
                for arq in lista:
                    os.chdir("Documentos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"/Documentos")

            for lista in self.listScr:
                for arq in lista:
                    os.chdir("Scripts")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"/Scripts")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")


    def copiarArq(self):
        try:
            for lista in self.listFoto:
                for arq in lista:
                    os.chdir("Fotos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"/Fotos")

            for lista in self.listVid:
                for arq in lista:
                    os.chdir("Vídeos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"/Vídeos")

            for lista in self.listMus:
                for arq in lista:
                    os.chdir("Músicas")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"/Músicas")

            for lista in self.listDoc:
                for arq in lista:
                    os.chdir("Documentos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"/Documentos")
            for lista in self.listScr:
                for arq in lista:
                    os.chdir("Scripts")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"/Scripts")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

shutill = shutil