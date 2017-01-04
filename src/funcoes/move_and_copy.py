# coding: utf-8
__author__ = "João Marcos S. e Araújo"
__email__ = "marcosjoao37@hotmail.com.br"

import shutil
import os
import glob
from src.funcoes.config import Config

class MoveAndCopy:

    def __init__(self):
        self.fileDict = {}
        conf = Config()
        self.fileDict = conf.loadDataTypes()

    def moveFiles(self, directory):
        for docType in self.fileDict:
            for fileExtension in self.fileDict[docType]:
                for file in glob.glob(directory + '*.' + fileExtension):
                    if(os.name == "posix"):
                        # Unix like...
                        if not directory.endswith("/"):
                            self.moveSingleFile(file, directory+docType+'/')
                        else:
                            self.moveSingleFile(file, directory+docType)
                    elif(os.name == "nt"):
                        # Windows like...
                        if not directory.endswith("\\"):
                            self.moveSingleFile(file, directory+docType+'\\')
                        else:
                            self.moveSingleFile(file, directory+docType)
                    else:
                        messagebox.showerror("ERROR","Opss... Could not determine your SO... Exiting... :(")
                        exit(0)

    def moveSingleFile(self, file, directory):
        try:
            try:
                os.mkdir(directory)
            except:
                pass
            if not os.path.exists(directory+file):
                shutil.move(file, directory)
            else:
                print("WARNING: can't MOVE file '"+file+"'' because it already exists inside '"+directory+"'.")
        except:
            print("ERROR: can't MOVE file '"+file+"'' to directory '"+directory+"'.")
            pass

    def copyFiles(self, directory):
        for docType in self.fileDict:
            for fileExtension in self.fileDict[docType]:
                for file in glob.glob(directory + '*.' + fileExtension):
                    if(os.name == "posix"):
                        # Unix like...
                        if not directory.endswith("/"):
                            self.copySingleFile(file, directory+docType+'/')
                        else:
                            self.copySingleFile(file, directory+docType)
                    elif(os.name == "nt"):
                        # Windows like...
                        if not directory.endswith("\\"):
                            self.copySingleFile(file, directory+docType+'\\')
                        else:
                            self.copySingleFile(file, directory+docType)
                    else:
                        messagebox.showerror("ERROR","Opss... Could not determine your OS... Exiting... :(")
                        exit(0)

    def copySingleFile(self, file, directory):
        try:
            try:
                os.mkdir(directory)
            except:
                pass
            if not os.path.exists(directory+file):
                shutil.copy2(file, directory)
            else:
                print("WARNING: can't COPY file '"+file+"'' because it already exists inside '"+directory+"'.")
        except:
            print("ERROR: can't COPY file '"+file+"'' to directory '"+directory+"'.")
            pass