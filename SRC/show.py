import sqlite3 as sq
from tkinter import *
import SRC.encrypt_decrypt as ed
import SRC.design as des

accounts = []
fulllist = []
des.primary_color = '#212120'

mypassword = '123'

import os
import sys

def resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS  # Folder PyInstaller extracts to
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Example usage
dbdir = resource_path("DATABASE/maindb.db")





#dbdir = "DATABASE/maindb.db"
dbconnection = sq.connect(dbdir)
dbcursor = dbconnection.cursor()

extractacc_query = '''SELECT Account FROM PASSWORDS'''
extractemailid_query = '''SELECT Email_ID FROM PASSWORDS'''
extractpass_query = '''SELECT Password FROM PASSWORDS'''
completequery = '''SELECT * FROM PASSWORDS'''


def extract_data(acc):
    
    
    
    dbcursor.execute(completequery)
    output = dbcursor.fetchall()
    for row in output:
        if row[0] == acc:
            fulllist.append(row)
            
    return fulllist

        
def fetchall_query():
    dbcursor.execute(completequery)
    output = dbcursor.fetchall()
    return output
        
def showtablelist():
    output = fetchall_query()
    tablelist = []

    for row in output:
        listrow = (row[0], row[1])
        tablelist.append(listrow)
        
    #print(tablelist)
    return tablelist


def show_password(values):
    
    
    truepass=''
    truelist = []
    print(values)
    output = fetchall_query()
    for row in output:
        listrow = (row[0], row[1])
        if listrow==values:
            truelist.append(row[0])
            truelist.append(row[1])
            truepass = ed.encrypt_decrypt(row[2])
            truelist.append(truepass)
            
    revealpass(truelist)
            
    
    
    
    
    
    
def passwordUI(values):
    
    
    
    #--------------------SUBMIT COMMAND---------------------------
    
    def submitcomm(): 
                
        if passentry.get()==conpassentry.get()==mypassword:
            root.destroy()
            show_password(values)
    
    #---------------------END SUBMIT-----------------------------------
    

    
    
    
    #--------------------MAIN UI----------------------------------
    
    root = Tk()
    root.resizable(FALSE, FALSE)
    root.title('PASSWORD DATABASE')
    root.geometry("300x250")
    root.config(bg=des.primary_color)
    
    win = Canvas(root, bg=des.primary_color, highlightbackground=des.primary_color,
                 highlightcolor=des.primary_color,
                 highlightthickness=0)
    win.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
    
    

    
    passlabel = Label(win, text="Password", bg=des.primary_color, fg='white')
    passlabel.grid(row=0, column=0)
    
    passconlabel = Label(win, text="Confirm\nPassword", bg=des.primary_color, fg='white')
    passconlabel.grid(row=1, column=0)
    
    passentry = Entry(win, width=40, show='*')
    passentry.grid(row=0, column=1, padx=10, pady=10)
    
    conpassentry = Entry(win, width=40, show='*')
    conpassentry.grid(row=1, column=1, padx=10, pady=10)
    
    submitbutton = Button(win, des.buttonconfig, text="Submit", command=submitcomm)
    submitbutton.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.8)
    
    
    
    #---------------END OF MAIN UI-----------------------------
    
    win.mainloop()
    
    
    
    
    
    

def revealpass(truelist):
    win = Tk()
    win.geometry('200x200')
    win.resizable(FALSE, FALSE)
    win.config(bg=des.primary_color)
    Label(win, des.label_config, text=truelist[0]).grid(row=0, column=0, padx=20, pady=10)
    Label(win, des.label_config, text=truelist[1]).grid(row=1, column=0, padx=20, pady=10)
    Label(win, des.label_config, text=truelist[2]).grid(row=2, column=0, padx=20, pady=10)
    
    win.after(3000, win.destroy)
    
    win.mainloop()


