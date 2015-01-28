# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'
# Organizador em pastas de acordo com os seus respectivos tipos.
# .jpg, .png, .bmp para a pasta fotos; .flv, .wmv, .mp4 para a pasta vídeos e etc.

from tkinter import messagebox
import shutil
import glob
import os

class Ogar:

    def __init__(self):
        pass

    """
    A principal tarefa desta função {leituraArq()} é a de criar listas com os nomes dos arquivos da pasta para qual o
    programa foi apontado. Por exemplo, ele gerará a lista self.listFoto com o nome do diretório completo das imagens
    que estão na pasta. Ex: Na pasta "/home/usuario/Downloads", existe um arquivo chamado "foto.jpg", logo, gerará uma
    trupla na lista chamada "/home/usuario/Downloads/foto.jpg". Os parâmetros 'esc' e 'dir' são referentes à outra
    classe, 'esc' referente a ESCOLHA de COPIAR ou MOVER or arquivos; 'dir' referente ao DIRETÓRIO onde estarão os
    arquivos, que será capturado na área de texto da interface TK, presente no arquivo InterfaceOgarq.py.
    Para entender algumas funções, olhe-as lá em baixo antes de ver o código principal.
    """
    def leituraArq(self, esc, dir):

        #Verificação de existência do diretório.
        self.procDir(dir)

        #Verificação de existência de pastas com o mesmo nome, se não, faz a criação das pastas.
        self.criarPastas()

        #Criação das listas com o nome do diretório completo mais o nome do arquivo. Ex: /home/usr/Downloads/foto.jpg.
        self.listFoto = [] # cria uma lista vazia
        ext = 'jpg,png,bmp,jpeg,gif'.split(',') # ext é a variavel que conterá as extensões de arquivos de imagem
        for i in ext: # percorre todos os elementos da lista ext
            for j in glob.glob(self.dir+'*.' + i): # percorre todas das ocorrencias de arquivos com extensão de imagem
                self.listFoto.append(j) # salva o caminho dos arquivos de imagem na lista self.listFoto

        self.listMus = []
        ext = 'mp3,wav,flac,aac'.split(',')
        for i in ext:
            for j in glob.glob(self.dir+'*.' + i):
                self.listMus.append(j)

        self.listVid= []
        ext = 'wmv,mp4,mkv,rmvb,flv,3gp,avi,mov'.split(',')
        for i in ext:
            for j in glob.glob(self.dir+'*.' + i):
                self.listVid.append(j)

        self.listScr= []
        ext = 'sh,py,java,bat'.split(',')
        for i in ext:
            for j in glob.glob(self.dir+'*.' + i):
                self.listScr.append(j)

        self.listDoc= []
        ext = 'doc,docx,txt,odt'.split(',')
        for i in ext:
            for j in glob.glob(self.dir+'*.' + i):
                self.listDoc.append(j)

        self.listComp= []
        ext = 'rar,zip,7zip,tar.gz,tar.gx'.split(',')
        for i in ext:
            for j in glob.glob(self.dir+'*.' + i):
                self.listComp.append(j)

        self.listExe= []
        ext = 'exe,run,msi'.split(',')
        for i in ext:
            for j in glob.glob(self.dir+'*.' + i):
                self.listExe.append(j)                

        #Fim da criação.

        #Alguns testes para debbuger.
        print("após as listas.")
        print(self.listFoto)
        print(esc)
        #Fim testes.

        #Verificação da escolha (COPIAR ou MOVER) e execução da função escolhida pelo usuário.
        try:
            messagebox.showinfo("INFORMAÇÃO","AGUARDE...")
            if esc == "1":
                print("1")
                self.moverArq()
            elif esc == "2":
                print("2")
                self.copiarArq()

            #Uma pequena janela com informações.
            messagebox.showinfo("INFORMAÇÃO","TUDO PRONTO E ORGANIZADO!")
        except:
            #Uma pequena janela com informações.
            messagebox.showinfo("INFORMAÇÃO","OPSS... ALGO DEU ERRADO.")

    """
    A função {criarPastas()} faz o que o próprio nome diz: Ceia as pastas necessárias para a execução das outras
    funções, são elas COPIAR ou MOVER. Cria pastas dentro do diretório apontado.
    """
    def criarPastas(self):
        #Se está pasta padrão do programa, posterior com dois undercores, ainda não existir na pasta, quer dizer que
        #é a primeira que o programa é executado alí.
        try:
            os.mkdir(self.dir+"Fotos_"), os.mkdir(self.dir+"Vídeos_"), os.mkdir(self.dir+"Documentos_"), \
            os.mkdir(self.dir+"Músicas_"), os.mkdir(self.dir+"Compactados_"), os.mkdir(self.dir+"Executáveis_"), \
            os.mkdir(self.dir+"Scripts_")

        except:
            messagebox.showinfo("INFORMAÇÃO","PASTAS  JÁ EXISTENTES.")
            print("Pastas já existentes.")

    """
    As funções {moverArq()} e {copiarArq()} fazem e tem quase a/o mesma coisa/código. Mudam-se apenas algumas linhas,
    tais elas são nos comandos shutill.move e shutill.copy2, o primeiro para mover, o segundo para copiar.
    Ainda há também uma pequena lógica no código, que serve para separar apenas o nome do arquivo para fazer a sua
    cópia ou para movê-lo. Primeiro separo uma lista que está dentro da "lista pai", a qual é self.listFoto.
    self.listFoto é composto de listas dentro de listas. Logo após, separo os nomes dos arquivos que há em cada lista
    (ainda com o nome do diretório inteiro).
    Em (arq.split("/"))[-1] separo apenas o nome do arquivo. Ex: "/home/usr/Downloads/foto.jpg" -> "foto.jpg".
    Logo após, o programa entra na pasta, verifica se já existe um arquivo com o nome igual. Se não, COPIA ou MOVE
    o arquivo para dentro da basta. Após cada função de COPIAR ou MOVER, o programa sai da pasta, voltando a pasta
    raiz dada ao programa. Ex: "/home/usr/Downloads/Fotos/foto.jpg" -> "/home/usr/Downloads".
    Faz-se isto com todos os arquivos, em todas as pastas.
    """
    def moverArq(self):
        try:
            print(self.listFoto)
            for arq in self.listFoto:
                arq = (arq.split("/"))[-1]
                #Alguns testes para debbuger.
                print(arq)
                #Fim testes.
                os.chdir(self.dir+"Fotos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Fotos_")

            for arq in self.listVid:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Vídeos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Vídeos_")

            for arq in self.listMus:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Músicas_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Músicas_")

            for arq in self.listDoc:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Documentos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Documentos_")

            for arq in self.listComp:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Compactados_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Compactados_")

            for arq in self.listExe:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Executáveis_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Executáveis_")

            for arq in self.listScr:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Scripts_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Scripts_")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def copiarArq(self):
        try:
            for arq in self.listFoto:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Fotos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.copy2(arq, self.dir+"Fotos_")

            for arq in self.listVid:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Vídeos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.copy2(arq, self.dir+"Vídeos_")

            for arq in self.listMus:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Músicas_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.copy2(arq, self.dir+"Músicas_")

            for arq in self.listDoc:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Documentos_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.copy2(arq, self.dir+"Documentos_")

            for arq in self.listComp:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Compactados_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.copy2(arq, self.dir+"Compactados_")

            for arq in self.listExe:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Executáveis_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.move(arq, self.dir+"Executáveis_")

            for arq in self.listScr:
                arq = (arq.split("/"))[-1]
                os.chdir(self.dir+"Scripts_")
                if os.path.exists(arq):
                    print("Arquivo já existente.")
                    os.chdir("..")
                else:
                    os.chdir("..")
                    shutill.copy2(arq, self.dir+"Scripts_")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    """
    Verifica a consistência do diretório dado ao programa. Além de fornecer ou não uma barra {"/"}, caso o usuário não
    forneça, como no primeiro caso.
    """
    def procDir(self, dir):
        if dir[-1] != "/":
            dir = dir+"/"

        if os.path.isdir(dir):
            self.dir = dir
            messagebox.showinfo("INFORMAÇÃO","DIRETÓRIO ENCONTRADO!")
            return True
        else:
            messagebox.showinfo("INFORMAÇÃO","OPSS... DIRETÓRIO NÃO ENCONTRADO!")
            return False


shutill = shutil
message = messagebox
