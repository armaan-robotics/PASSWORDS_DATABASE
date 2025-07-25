from tkinter import *
from tkinter import messagebox
import sqlite3
import SRC.encrypt_decrypt as ed
import SRC.design as des
import os
import sys

des.primary_color = '#212120'

des.buttonconfig = {
    'bd': 0,
    'bg': 'cyan',
    'highlightbackground': des.primary_color,
    'highlightcolor': des.primary_color,
    'highlightthickness': 0
}









def makenew():
    
    
    #----------------------------makenew command------------------------------

    def makenew_command(acc, emailid, encrypted_password):
        
        


        def resource_path(relative_path):
            """Get the absolute path to the resource, works for dev and for PyInstaller"""
            try:
                base_path = sys._MEIPASS  # Folder PyInstaller extracts to
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        # Example usage
        dbdir = resource_path("DATABASE/maindb.db")

        
        dbconnect = sqlite3.connect(dbdir)
        dbcursor = dbconnect.cursor()
        
        dbcursor.execute("INSERT INTO PASSWORDS VALUES(?,?,?)",(acc, emailid, encrypted_password))
        
        dbconnect.commit()
        dbconnect.close()
        
        

    #-----------------------------makenew command end-----------------

    
    
    
    
    #--------------------SUBMIT COMMAND---------------------------
    
    def submitcomm():
        
        acc = accentry.get()
        emailid = emailentry.get()
        
        
        
        if passentry.get()==conpassentry.get():
            rawpass = passentry.get()
            password = ed.encrypt_decrypt(rawpass)
            root.destroy()
            messagebox.showinfo('PASSWORDS', 'New account & password registered !')
            makenew_command(acc, emailid, password)
            
        else:
            messagebox.showerror('PASSWORDS', 'Both passwords do not match or are wrong !')
    
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
    
    acclabel = Label(win, text="Account", bg=des.primary_color, fg='white')
    acclabel.grid(row=0, column=0)
    
    emaillabel = Label(win, text="Linked Email", bg=des.primary_color, fg='white')
    emaillabel.grid(row=1, column=0)
    
    passlabel = Label(win, text="Password", bg=des.primary_color, fg='white')
    passlabel.grid(row=2, column=0)
    
    passlabel = Label(win, text="Confirm\nPassword", bg=des.primary_color, fg='white')
    passlabel.grid(row=3, column=0)
    
    accentry = Entry(win, width=40)
    accentry.grid(row=0, column=1, padx=10, pady=10)
    
    emailentry = Entry(win, width=40)
    emailentry.grid(row=1, column=1, padx=10, pady=10)
    
    passentry = Entry(win, width=40, show='*')
    passentry.grid(row=2, column=1, padx=10, pady=10)
    
    conpassentry = Entry(win, width=40, show='*')
    conpassentry.grid(row=3, column=1, padx=10, pady=10)
    
    submitbutton = Button(win, des.buttonconfig, text="Submit", command=submitcomm)
    submitbutton.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.8)
    
    
    
    #---------------END OF MAIN UI-----------------------------
    
    win.mainloop()