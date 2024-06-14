from tkinter import *


#Окно
root = Tk()
root.title("Colors Palette")
root.geometry("300x480")
root.resizable(width=False, height=False)
root['bg'] = 'pink'

#Функции



def open_win1():
    win1 = Toplevel()
    win1.geometry('450x300')
    win1.grab_set()
    win1.resizable(width=False, height=False)
    win1['bg'] = '#b8b8b8'
    l1 = Label(win1,
               text='hex: #B8B8B8/ rgb(184, 184, 184)/ hsl(0, 0%, 72%)',
               font=('bahnschrift', 10),
               bg='#B8B8B8'
               )

    l1.pack(expand=1)

def open_win2():
    win2 = Toplevel()
    win2.geometry('450x300')
    win2.grab_set()
    win2.resizable(width=False, height=False)
    win2['bg'] = '#9a93b7'
    l2 = Label(win2,
               text='hex: #9A93B7/ rgb(154, 147, 183)/ hsl(252, 20%, 65%)',
               font=('bahnschrift', 10),
               bg='#9A93B7'
               )
    l2.pack(expand=1)

def open_win3():
    win3 = Toplevel()
    win3.geometry('450x300')
    win3.grab_set()
    win3.resizable(width=False, height=False)
    win3['bg'] = '#6d7d7a'
    l3 = Label(win3,
               text='hex: #6D7D7A/ rgb(109, 125, 122)/ hsl(169, 7%, 46%)',
               font=('bahnschrift', 10),
               bg='#6D7D7A'
               )
    l3.pack(expand=1)

def open_win4():
    win4 = Toplevel()
    win4.geometry('450x300')
    win4.grab_set()
    win4.resizable(width=False, height=False)
    win4['bg'] = '#5D5B68'
    l4 = Label(win4,
               text='hex: #5D5B68/ rgb(93, 91, 104)/ hsl(249, 7%, 38%)',
               font=('bahnschrift', 10),
               bg='#5D5B68'

               )
    l4.pack(expand=1)


def open_win5():
    win5 = Toplevel()
    win5.geometry('450x300')
    win5.grab_set()
    win5.resizable(width=False, height=False)
    win5['bg'] = '#3A3A3A'
    l5 = Label(win5,
               text='hex: #3A3A3A/ rgb(58, 58, 58)/ hsl(0, 0%, 23%)',
               font=('bahnschrift', 10),
               bg='#3A3A3A'

               )
    l5.pack(expand=1)


def open_win6():
    win6 = Toplevel()
    win6.geometry('450x300')
    win6.grab_set()
    win6.resizable(width=False, height=False)
    win6['bg'] = '#5E8B9C'
    l6 = Label(win6,
               text='hex: #5E8B9C/ rgb(94, 139, 156)/ hsl(196, 25%, 49%',
               font=('bahnschrift', 10),
               bg='#5E8B9C'

               )
    l6.pack(expand=1)


def open_win7():
    win7 = Toplevel()
    win7.geometry('450x300')
    win7.grab_set()
    win7.resizable(width=False, height=False)
    win7['bg'] = '#423D5E'
    l7 = Label(win7,
               text='hex: #423D5E/ rgb(66, 61, 94)/ hsl(249, 21%, 30%',
               font=('bahnschrift', 10),
               bg='#423D5E'

               )
    l7.pack(expand=1)


def open_win8():
    win8 = Toplevel()
    win8.geometry('450x300')
    win8.grab_set()
    win8.resizable(width=False, height=False)
    win8['bg'] = '#7f4483'
    l8 = Label(win8,
               text='hex: #7F4483/ rgb(127, 68, 131)/ hsl(296, 32%, 39%)',
               font=('bahnschrift', 10),
               bg='#7f4483'
               )
    l8.pack(expand=1)



#Кнопки

first1 = Button(root,
             text = '@ ~ @',
             command = open_win1,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#b8b8b8'
             )

second2 = Button(root,
             text = '@ ~ @',
             command = open_win2,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#9a93b7'
             )

third3 = Button(root,
             text = '@ ~ @',
             command = open_win3,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#6d7d7a'
             )

four4 = Button(root,
             text = '@ ~ @',
             command = open_win4,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#5d5b68'
             )

five5 = Button(root,
             text = '@ ~ @',
             command = open_win5,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#3a3a3a'
             )

six6 = Button(root,
             text = '@ ~ @',
             command = open_win6,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#5e8b9c'
             )

seven7 = Button(root,
             text = '@ ~ @',
             command = open_win7,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#423d5e'
             )

eight8 = Button(root,
             text = '@ ~ @',
             command = open_win8,
             font = ('bahnschrift',15),
             padx=100,
             pady=10,
             bg = '#7f4483'
             )

#Вывод

first1.pack()
second2.pack()
third3.pack()
four4.pack()
five5.pack()
six6.pack()
seven7.pack()
eight8.pack()




root.mainloop()