from tkinter import *
from tkinter import messagebox
from src.funcoes.config import Config


class Settings:
    def __init__(self, root):
        self.root = root
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.title('Settings')
        self.window.eval("tk::PlaceWindow %s center" %
                             self.window.winfo_pathname(self.window.winfo_id()))
        self.conf = Config()

        Label(self.window, text='Directories names').grid(
            row=1, column=1, stick=W, pady=5, padx=(10, 0))
        Label(self.window, text='Extensions names').grid(
            row=1, column=2, stick=W, pady=5, padx=(5, 10))
        row_count = 2

        fileDict = self.conf.loadDataTypes()
        self.docTypeEntryList = []
        self.fileExtensionEntryList = []
        for docType in fileDict:
            docTypeEntry = Entry(self.window)
            self.docTypeEntryList.append(docTypeEntry)
            docTypeEntry.grid(row=row_count, column=1,
                              stick=W, pady=5, padx=(10, 0))
            docTypeEntry.insert(0, docType)
            filesEntry = ''
            for fileExtension in fileDict[docType]:
                filesEntry += fileExtension + ','
            filesEntry = filesEntry[0:-1]
            fileExtensionEntry = Entry(self.window)
            self.fileExtensionEntryList.append(fileExtensionEntry)
            fileExtensionEntry.grid(
                row=row_count, column=2, stick=W + E, pady=5, padx=(5, 10))
            fileExtensionEntry.insert(0, filesEntry)
            row_count += 1

        action_buttons = Frame(self.window)
        action_buttons.grid(row=row_count, column=2, stick=E, pady=5, padx=(0, 10))
        Button(action_buttons, command=self.save_settings,
               text='Save').pack(expand=True, fill=X, side=RIGHT)
        Button(action_buttons, command=self.window.destroy,
               text='Cancel').pack(expand=True, fill=X, side=RIGHT)


    def save_settings(self):
        userSettings = {}
        count = 0
        while(count < len(self.docTypeEntryList)):
            userSettings[self.docTypeEntryList[count].get(
            )] = self.fileExtensionEntryList[count].get().split(',')
            count += 1
        result = self.conf.updateJsonData(userSettings)
        if(result):
            messagebox.showinfo("INFORMATION", "Settings saved!")
            self.window.destroy()
        else:
            messagebox.showinfo(
                "INFORMATION", "Opss... Can't save your configurations...")
