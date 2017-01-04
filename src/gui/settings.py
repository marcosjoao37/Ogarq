from tkinter import *
from tkinter import messagebox
from src.funcoes.config import Config

class Settings:
	def __init__(self, parent):
		self.parent = parent
		self.conf = Config()

		Label(self.parent, text='Directories names').grid(row=1, column=1, stick=W, pady=5)
		Label(self.parent, text='Extensions names').grid(row=1, column=2, stick=W, pady=5)
		row_count = 2

		fileDict = self.conf.loadDataTypes()
		self.docTypeEntryList = []
		self.fileExtensionEntryList = []
		for docType in fileDict:
			docTypeEntry = Entry(self.parent)
			self.docTypeEntryList.append(docTypeEntry)
			docTypeEntry.grid(row=row_count, column=1, stick=W, pady=5)
			docTypeEntry.insert(0, docType)
			filesEntry = ''
			for fileExtension in fileDict[docType]:
				filesEntry += fileExtension + ','
			filesEntry = filesEntry[0:-1]
			fileExtensionEntry = Entry(self.parent)
			self.fileExtensionEntryList.append(fileExtensionEntry)
			fileExtensionEntry.grid(row=row_count, column=2, stick=W+E, pady=5)
			fileExtensionEntry.insert(0, filesEntry)
			row_count+=1

		Button(self.parent, command=self.save_settings, text='Save').grid(row=row_count, column=2, stick=W, pady=5)
		Button(self.parent, command=self.parent.destroy, text='Cancel').grid(row=row_count, column=1, stick=W, pady=5)

	def save_settings(self):
		userSettings = {}
		count = 0
		while(count<len(self.docTypeEntryList)):
			userSettings[self.docTypeEntryList[count].get()] = self.fileExtensionEntryList[count].get().split(',')
			count+=1
		result = self.conf.updateJsonData(userSettings)
		if(result):
			messagebox.showinfo("INFORMATION","Settings saved!")
		else:
			messagebox.showinfo("INFORMATION","Opss... Can't save your new configurations...")