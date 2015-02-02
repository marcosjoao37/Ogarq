# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'

from tkinter import messagebox
import shutil
import os

class MoverECopiar:
    def __init__(self):
        pass

    """
    As funções {moverArq()} e {copiarArq()} fazem e tem quase a/o mesma/mesmo coisa/código. Mudam-se apenas algumas
    linhas,tais elas são nos comandos shutil.move e shutil.copy2, o primeiro para mover, o segundo para copiar.
    Ainda há também uma pequena lógica no código, que serve para separar apenas o nome do arquivo para fazer a sua
    cópia ou para movê-lo. Primeiro separo um nome da lista.
    Em (arq.split("/"))[-1] separo apenas o nome do arquivo. Ex: "/home/usr/Downloads/foto.jpg" -> "foto.jpg".
    Logo após, o programa entra na pasta, verifica se já existe um arquivo com o nome igual. Se não, COPIA ou MOVE
    o arquivo para dentro da basta. Após cada função de COPIAR ou MOVER, o programa sai da pasta, voltando a pasta
    raiz dada ao programa. Ex: "/home/usr/Downloads/Fotos/foto.jpg" -> "/home/usr/Downloads".
    Faz-se isto com todos os dda, em todas as pastas.
    """
    def moverArq(self, dir, comp, foto, exe, doc, mus, vid, scr):
        try:
            for arq in foto:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Fotos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Fotos_")

            for arq in vid:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Vídeos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Vídeos_")

            for arq in mus:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Músicas_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Músicas_")

            for arq in doc:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Documentos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Documentos_")

            for arq in comp:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Compactados_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Compactados_")

            for arq in exe:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Executáveis_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Executáveis_")

            for arq in scr:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Scripts_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Scripts_")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def copiarArq(self, dir, comp, foto, exe, doc, mus, vid, scr):
        try:
            for arq in foto:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Fotos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.copy2(arq, dir+"Fotos_")

            for arq in vid:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Vídeos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.copy2(arq, dir+"Vídeos_")

            for arq in mus:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Músicas_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.copy2(arq, dir+"Músicas_")

            for arq in doc:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Documentos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.copy2(arq, dir+"Documentos_")

            for arq in comp:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Compactados_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.copy2(arq, dir+"Compactados_")

            for arq in exe:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Executáveis_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.move(arq, dir+"Executáveis_")

            for arq in scr:
                arq = (arq.split("/"))[-1]
                os.chdir(dir+"Scripts_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutil.copy2(arq, dir+"Scripts_")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

message = messagebox
