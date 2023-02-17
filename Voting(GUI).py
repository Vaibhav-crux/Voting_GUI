# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 03:56:04 2020

@author: #ASUR
"""
from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter as tk
m=tk.Tk()
m.geometry("1924x1024")
m.configure(bg='grey')
#m.iconbitmap(r'D:\1.jpg')
uo=tk.Label(m)
l=0
l1=0
def gn(): 
    global l
    l+=1
def jp():
    global l1
    l1+=1
def done():
    Msg=tk.messagebox.askquestion("Exit Application","Are you sure you exit application")
    if Msg=='yes':
        i=tk.Label(m,text='The total vote of G.N :  = '+str(l)+' Votes',bg='grey')
        i.pack()
        h=tk.Label(m,text='The total vote of J.P.E.A :  = '+str(l1)+' Votes',bg='grey')
        h.pack()      
        if(l>l1):       
            z=l-l1
            k=tk.Label(m,text='G.N wins by '+str(z)+' votes',bg='green')
            k.pack()
        if(l1>l):
            z=l1-l
            x=tk.Label(m,text='J.P.E.A wins by '+str(z)+' votes',bg='green')
            x.pack()
        if(l==l1):
            x=tk.Label(m,text='Tye')
            x.pack()
        qq=tk.Label(text='--------',bg='grey')
        qq.pack()
        q4=tk.Button(text='Graph',width=5,command=Graph)
        q4.pack() 
    else:
        print("hi")
def Graph():
    si=[l,l1]
    la='G.N','J.P.E.A'
    col='red','silver'
    plt.pie(si,labels=la,colors=col,autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('books_read.png') #Save's The Data
    plt.show()    # stops mainloop
    m.destroy()
    
m.wm_title('VOTING')
q1=tk.Button(text="G.N",bd=5,width=7,bg='orange',fg='white',
             activebackground='red',command=gn)
q1.pack()
qq=tk.Label(text='--------',bg='grey')
qq.pack()
q2=tk.Button(text="J.P.E.A",bd=5,width=7,bg='orange',fg='white',
             activebackground='red',command=jp)
q2.pack()
qq=tk.Label(text='--------',bg='grey')
qq.pack()
q3=tk.Checkbutton(text='Done',command=done,bg='yellow',fg='purple')
q3.pack()
m.mainloop()
