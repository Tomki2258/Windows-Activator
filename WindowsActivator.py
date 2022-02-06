from cgitb import text
import tkinter as tk
import os
from tkinter import font as tkFont

window = tk.Tk()
window.title('Windows 10/11 activator')
font = tkFont.Font(family='Helvetica', size=24)
window.configure(bg='#133C55')

tk.Label(text="Windows Activator",font=tkFont.Font(family='Helvetica', size=24),bg='#133C55',fg='#EBEBEB').grid(column=1, row=0)


def active(option):
    #Windows home activation
    if(option=='home'):
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms s8.uk.to")
        os.system("slmgr /ato")
    #Windows PRO activation
    elif(option=='pro'):
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms s8.uk.to")
        os.system("slmgr /ato")
        print('cos')
   

home = tk.Button(text="home" ,font=tkFont.Font(family='Helvetica', size=16),bg='#59A5D8',fg='#EBEBEB', command=lambda : active('home')).grid(column=1,row=1)
pro = tk.Button(text="pro" ,font=tkFont.Font(family='Helvetica', size=16),bg='#59A5D8',fg='#EBEBEB', command=lambda : active('pro')).grid(column=1,row=2)



window.mainloop()