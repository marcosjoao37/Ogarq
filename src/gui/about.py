from tkinter import *

class About:
	def __init__(self, parent):
		self.parent = parent
		self.title = ('Times', '20', 'bold')
		self.subtitle = ('Times', '12', 'italic')
		self.fonte = ('Verdana', '10')

		Label(self.parent, text='OGARQ', font=self.title).grid(row=1, column=1, stick=E+W, pady=5)
		Label(self.parent, text='Organize your files on a fast and simple way.', font=self.subtitle).grid(row=2,
			column=1, stick=E+W, pady=5)
		Label(self.parent, text='Using: Python 3.x & TKinter', font=self.fonte).grid(row=3, column=1,
			stick=E+W, pady=5, padx=10)
		self.developer = 'Developer: João Marcos S. e Araújo\nE-mail: marcosjoao377@gmail.com\nProject: https://github.com/marcosjoao37/Ogarq\nBrazil'
		Label(self.parent, text=self.developer, font=self.fonte).grid(row=4, column=1, pady=5)
