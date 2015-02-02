# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'

import glob

from funcoes.TratamentoDePastas import TratamentoDePastas


"""
Dicionário com o nome de todas as extensões de dda.
"""

class DicionarioDeArquivos:
    def __init__(self):
        # Tipos de dda
        """
        self.Comp = 'rar,zip,7zip,tar.gz,tar.gx,7z,gzip'.split(',')
        self.Foto = 'jpg,png,bmp,jpeg,gif'.split(',')
        self.Exe = 'exe,run,msi,app,apk,deb,jar'.split(',')
        self.Doc = 'doc,docx,txt,odt,cad,pdf,xlsx,xls,csv,tsv,ppt,pptx,epub,docm,dot,dotx,xps'.split(',')
        self.Mus = 'mp3,wav,flac,aac'.split(',')
        self.Vid = 'wmv,mp4,mkv,rmvb,flv,3gp,avi,mov'.split(',')
        self.Scr = 'sh,py,java,bat,c,cs,php,vb,vbs,cpp,html'.split(',')
        """

        self.fileDict = {"Fotos_" : 'jpg,png,bmp,jpeg,gif',
                         "Compactados_" : 'rar,zip,7zip,tar.gz,tar.gx,7z,gzip',
                         "Executáveis_" : 'exe,run,msi,app,apk,deb,jar',
                         "Scripts_" : 'sh,py,java,bat,c,cs,php,vb,vbs,cpp,html',
                         "Documentos_" : 'doc,docx,txt,odt,cad,pdf,xlsx,xls,csv,tsv,ppt,pptx,epub,docm,dot,dotx,xps',
                         "Músicas_" : 'mp3,wav,flac,aac',
                         "Vídeos_" : 'wmv,mp4,mkv,rmvb,flv,3gp,avi,mov'
        }

        """
    A principal tarefa desta função {leituraEsc()} é a de criar listas com os nomes dos dda da pasta para qual o
    programa foi apontado. Por exemplo, ele gerará a lista self.listFoto com o nome do diretório completo das imagens
    que estão na pasta. Ex: Na pasta "/home/usuario/Downloads", existe um arquivo chamado "foto.jpg", logo, gerará uma
    trupla na lista chamada "/home/usuario/Downloads/foto.jpg". Os parâmetros 'esc' e 'dir' são referentes à outra
    classe, 'esc' referente a ESCOLHA de COPIAR ou MOVER or dda; 'dir' referente ao DIRETÓRIO onde estarão os
    dda, que será capturado na área de texto da interface TK, presente no arquivo io/InterfaceOgarq.py.
    """
    def dicionarioDeArquivos(self, dir):

        # Verificação de existência do diretório.
        if tdp.procDir(dir):
            # Criação das listas com o nome do diretório completo mais o nome do arquivo.
            # Ex: /home/usr/Downloads/foto.jpg.

            # Listas vazias para listar dda
            self.listComp = []
            self.listFoto = []
            self.listExe = []
            self.listDoc = []
            self.listMus = []
            self.listVid = []
            self.listScr = []

            self.dir2 = tdp.dir

            # Ext é a variavel que conterá as extensões de dda de imagem

            for docType in self.fileDict:
                for extensao in docType:
                    for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listFoto.append(arquivo)

            for extensao in self.Foto:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listFoto.append(arquivo)

            for extensao in self.Mus:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listMus.append(arquivo)

            for extensao in self.Vid:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listVid.append(arquivo)

            for extensao in self.Scr:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listScr.append(arquivo)

            for extensao in self.Doc:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listDoc.append(arquivo)

            for extensao in self.Comp:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listComp.append(arquivo)

            for extensao in self.Exe:
                for arquivo in glob.glob(tdp.dir+'*.' + extensao):
                    self.listExe.append(arquivo)
            # Fim da criação.

            # Verificação de existência de pastas com o mesmo nome, se não, faz a criação das pastas.
            tdp.criarPastas(self.listComp, self.listFoto, self.listExe, self.listDoc, self.listMus,
                            self.listVid, self.listScr)

            return True

        else:
            return False

tdp = TratamentoDePastas()