# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'

from tkinter import messagebox
import shutil
import os
import glob
from funcoes.DicionarioDeArquivos import DicionarioDeArquivos

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
    def moverSingle(self, arq, dir):
        try:
            try:
                print (dir)
                os.mkdir(dir)
            except:
                pass
            os.chdir(dir)

            if os.path.exists(arq):
                print("Arquivo já existente.")
                os.chdir("..")
            else:
                os.chdir("..")
                shutil.move(arq, dir)
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def moverArq(self, dir):
        for docType in DicionarioDeArquivos.fileDict:
            print (docType)
            for extensao in DicionarioDeArquivos.fileDict[docType].split(','):
                for arquivo in glob.glob('*.' + extensao):
                    #self.listFoto.append(arquivo)
                    self.moverSingle(arquivo, dir+"/"+docType)

    def copiarSingle(self, arq, dir):
        try:
            try:
                print (dir)
                os.mkdir(dir)
            except:
                pass
            os.chdir(dir)

            if os.path.exists(arq):
                print("Arquivo já existente.")
                os.chdir("..")
            else:
                os.chdir("..")
                #shutil.move(arq, dir)
                shutil.copy2(arq, dir)
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def copiarArq(self, dir):
        for docType in DicionarioDeArquivos.fileDict:
            print (docType)
            for extensao in DicionarioDeArquivos.fileDict[docType].split(','):
                for arquivo in glob.glob('*.' + extensao):
                    #self.listFoto.append(arquivo)
                    self.copiarSingle(arquivo, dir+"/"+docType)




message = messagebox
