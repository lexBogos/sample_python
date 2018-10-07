import os
import tkinter as tk
from tkinter import ttk
import sqlite3
import sys
import xlrd
from itertools import chain
from fnmatch import fnmatch 
import re
import win32api

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Поиск директории на всех дисках', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'place', 'boiler', 'costs', 'total'), height=30, show='headings')

        self.tree.column('ID', width=150, anchor=tk.CENTER)
        self.tree.column('description', width=100, anchor=tk.CENTER)
        self.tree.column('place', width=200, anchor=tk.CENTER)
        self.tree.column('boiler', width=200, anchor=tk.CENTER)
        self.tree.column('costs', width=500, anchor=tk.CENTER)
        self.tree.column('total', width=200, anchor=tk.CENTER)

        self.tree.heading('ID', text='Номер ППР')
        self.tree.heading('description', text='Дата')
        self.tree.heading('place', text='Место')
        self.tree.heading('boiler', text='Агрегат')
        self.tree.heading('costs', text='Название')
        self.tree.heading('total', text='Выполнил')

        
        
        with open('my_file1.txt', "r") as my_file1:
            for stroka in my_file1:
                stroka_part = stroka.split(',')
                self.tree.insert("", '1', iid = stroka_part)
                self.tree.set(stroka_part,'ID',  stroka_part[1].rstrip('0').rstrip('.'))
                self.tree.set(stroka_part,'description', stroka_part[2])
                self.tree.set(stroka_part,'place', stroka_part[3])
                self.tree.set(stroka_part,'boiler', stroka_part[4])
                self.tree.set(stroka_part,'costs', stroka_part[6])
                self.tree.set(stroka_part,'total', stroka_part[7])




        self.tree.pack()

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Поиск')
        self.geometry('600x400+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='№ ППР или его название:')
        label_description.place(x=50, y=50)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50, width = 350)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Поиск')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>')



        self.grab_set()
        self.focus_set()



if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Поиск ППР")
    root.geometry("1400x500+300+200")
        # root.resizable(False, False)
    root.mainloop()
 
#https://ru.stackoverflow.com/questions/463862/%D0%9D%D0%B0%D0%B9%D1%82%D0%B8-%D1%84%D0%B0%D0%B9%D0%BB%D1%8B-%D0%BF%D0%BE-%D1%87%D0%B0%D1%81%D1%82%D0%B8-%D0%BF%D1%83%D1%82%D0%B8-%D0%BD%D0%B5-%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%BF%D0%BE-%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8-c-python
