from tkinter import *
import webbrowser


class About:
    def __init__(self, root):
        self.root = root
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.title('About')
        self.window.eval("tk::PlaceWindow %s center" %
                         self.window.winfo_pathname(self.window.winfo_id()))
        self.window.config(padx=10, pady=5)
        self.title = ('Times', '20', 'bold')
        self.subtitle = ('Times', '12', 'italic')
        self.fonte = ('Verdana', '10')

        Label(self.window, text='OGARQ', font=self.title).grid(
            row=1, column=1, stick=E + W)

        Label(self.window,
              text='Organize your files on a fast and simple way.',
              font=self.subtitle).grid(
                  row=2, column=1, stick=E + W, pady=(0, 30))

        self.using = 'Using: Python 3.x & TKinter'
        self.developer = 'João Marcos S. e Araújo'
        self.email = 'marcosjoao377@gmail.com'
        self.project_url = 'https://github.com/marcosjoao37/Ogarq'
        Label(self.window, text='' + self.using,
              font=self.fonte).grid(row=4, column=1, stick=W)
        Label(self.window, text='Developer: ' + self.developer,
              font=self.fonte).grid(row=5, column=1, stick=W)
        Label(self.window, text='E-mail: ' + self.email,
              font=self.fonte).grid(row=6, column=1, stick=W)
        Label(self.window, text='Project: ' + self.project_url,
              font=self.fonte).grid(row=7, column=1, stick=W)

        action_buttons = Frame(self.window)
        action_buttons.grid(row=9, column=1, stick=E, pady=5)
        Button(action_buttons, command=self.openLink,
               text='Github').pack(expand=True, fill=X, side=RIGHT)
        Button(action_buttons, command=self.window.destroy,
               text='Close').pack(expand=True, fill=X, side=RIGHT)

    def openLink(self):
        webbrowser.open_new(self.project_url)
