# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'

from tkinter import messagebox
import os


class TratamentoDePastas:
    def __init__(self):
        pass

    """
    A função {criarPastas()} faz o que o próprio nome diz: Cria as pastas necessárias para a execução das outras
    funções, são elas COPIAR ou MOVER. Cria pastas dentro do diretório apontado. Caso os tipos de dda de certo
    tipo não existam, não se criará uma pasta para eles.
    """
    def criarPastas(self, comp, foto, exe, doc, mus, vid, scr):
        try:
            print(self.dir)
            messagebox.showinfo("INFORMAÇÃO","CRIANDO PASTAS...")
            if comp != []:
                os.mkdir(self.dir+"Compactados_")
            if foto != []:
                os.mkdir(self.dir+"Fotos_")
            if exe != []:
                os.mkdir(self.dir+"Executáveis_")
            if doc != []:
                os.mkdir(self.dir+"Documentos_")
            if mus != []:
                os.mkdir(self.dir+"Músicas_")
            if vid != []:
                os.mkdir(self.dir+"Vídeos_")
            if scr != []:
                os.mkdir(self.dir+"Scripts_")

        except:
            print("Algumas pastas já existentes.")


    """
    Verifica a consistência do diretório dado ao programa. Além de fornecer ou não uma barra {"/"}, caso o usuário não
    forneça.
    """
    def procDir(self, dir):
        if not dir.endswith("/"):
            self.dir = dir+"/"

        if os.path.isdir(dir):
            messagebox.showinfo("INFORMAÇÃO","DIRETÓRIO ENCONTRADO!")
            return True
        else:
            messagebox.showerror("ERRO","OPSS... DIRETÓRIO NÃO ENCONTRADO!")
            return False

message = messagebox