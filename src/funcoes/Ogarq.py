# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'
# Organizador em pastas de acordo com os seus respectivos tipos.
# .jpg, .png, .bmp para a pasta fotos; .flv, .wmv, .mp4 para a pasta vídeos e etc.

from tkinter import messagebox
from funcoes.MoverECopiar import MoverECopiar
import os

class Ogar:

    def __init__(self):
        pass

    """
    A principal tarefa desta função {leituraEsc()} é a de criar listas com os nomes dos dda da pasta para qual o
    programa foi apontado. Por exemplo, ele gerará a lista self.listFoto com o nome do diretório completo das imagens
    que estão na pasta. Ex: Na pasta "/home/usuario/Downloads", existe um arquivo chamado "foto.jpg", logo, gerará uma
    trupla na lista chamada "/home/usuario/Downloads/foto.jpg". Os parâmetros 'esc' e 'dir' são referentes à outra
    classe, 'esc' referente a ESCOLHA de COPIAR ou MOVER or dda; 'dir' referente ao DIRETÓRIO onde estarão os
    dda, que será capturado na área de texto da interface TK, presente no arquivo src/gui/InterfaceOgarq.py.
    """
    def leituraEsc(self, esc, dir):
        if not dir.endswith("/"):
            dir = dir+"/"
            os.chdir(dir)

        # Verificação da escolha (COPIAR ou MOVER) e executa a função escolhida pelo usuário.
        try:
            messagebox.showinfo("INFORMAÇÃO","AGUARDE...")
            if esc == "1":
                print("1")
                mec.moverArq(dir)
            elif esc == "2":
                print("2")
                mec.copiarArq(dir)

            # Uma pequena janela com informações.
            messagebox.showinfo("INFORMAÇÃO","TUDO PRONTO E ORGANIZADO!")
        except Exception as ssw:
            print (ssw)
            # Outra pequena janela com informações.
            messagebox.showinfo("INFORMAÇÃO","OPSS... ALGO DEU ERRADO... OGARQ")

mec = MoverECopiar()
message = messagebox
