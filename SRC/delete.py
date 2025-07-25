import sqlite3 as sq
from tkinter import *
import SRC.design as des
from tkinter import messagebox

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




dbconnection = sq.connect(dbdir)
dbcursor = dbconnection.cursor()

global idno


extract_query = '''SELECT rowid, * FROM PASSWORDS'''
selectall_query = '''SELECT * FROM PASSWORDS'''
delete_query = '''DELETE FROM PASSWORDS WHERE rowid = ?'''


def deleterow(values):

    def submitcomm(): 
                
        if passentry.get()==conpassentry.get()==mypassword:
            root.destroy()
            
            
            
            dbcursor.execute(extract_query)
            output = dbcursor.fetchall()
            
            for row in output:
                listrow = (row[1], row[2])
                if listrow==values:
                    print(row[0])
                    dbcursor.execute(delete_query, (row[0],))
                    dbconnection.commit()
                    dbcursor.close()
                    dbconnection.close()
                    
            messagebox.showinfo('PASSWORDS', 'Deleted !')
    
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
    

    
            
    
