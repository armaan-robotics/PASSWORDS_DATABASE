from tkinter import *
from tkinter import ttk
import SRC.makenew as mn
import SRC.show as sh
import SRC.encrypt_decrypt as ed
import SRC.delete as dlt
import SRC.design as des




columnheading = ('Account', 'Linked Email ID')






#main function
def mainfunc():
    
    #------------------------------------SET ROOT----------------------------------
    
    root = Tk()
    root.title('PASSWORD DATABASE')
    root.geometry('1000x650')
    root.config(bg=des.primary_color)
    root.resizable(False, False)
    
    #------------------------END OF ROOT--------------------------------------------
    
    
    
    
    #------------------------------------TITLE CANVAS--------------------------------------
    
    titlecanvas = Canvas(root,
                         bg=des.primary_color,
                         highlightbackground=des.primary_color,
                         highlightcolor=des.primary_color)
    titlecanvas.place(relheight=0.1, relwidth=1, relx=0, rely=0)
    
    title = Label(titlecanvas, fg='white', bg=des.primary_color, font=('Roboto', 15), text="Password Database")
    title.place(relx=0.01, rely=0.2)
    
    createrlabel = Label(titlecanvas, bg=des.primary_color, fg='white', text="-Armaan Gupta")
    createrlabel.place(relx=0.85, rely=0.5)
    
    #---------------------------------END OF TITLE CAVAS-----------------------------------
    
    
    
    
    
    #-----------------------------------------MAIN CANVAS-------------------------------------
    
    maincanvas = Canvas(root, bg=des.primary_color,
                        highlightbackground=des.primary_color,
                        highlightcolor=des.primary_color)
    maincanvas.place(relheight=0.9, relwidth=0.9, relx=0, rely=0.1)
    
    
    def tablefunc():
        
        
        
                
        table = ttk.Treeview(maincanvas, columns=columnheading, show='headings')
        
        for col in columnheading:
            table.heading(col, text=col)
            table.column(col, width=350, stretch=FALSE)
            
        tablelist = sh.showtablelist()
        for i, row in enumerate(tablelist):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert('', END, values=row, tags=(tag,))
        table.place(relheight=0.8, relx=0.1, rely=0.1)
        

        # Styling
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview.Heading",
                        background=des.primary_color,
                        foreground='white',
                        font=('Arial', 12))

        style.configure("Treeview",
                        rowheight=30,
                        font=('Arial', 11, 'italic'),
                        borderwidth=0,
                        relief='flat')

        style.map('Treeview',
                background=[('selected', "#78bbff")],
                foreground=[('selected', 'white')])
        
        

        table.tag_configure('even', background="#dedede")
        table.tag_configure('odd', background='white')
                
        '''
        # Add vertical scrollbar
        scrollbar = ttk.Scrollbar(maincanvas, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        '''
    
        
        buttoncanvas = Canvas(root, bg=des.primary_color,
                            highlightbackground=des.primary_color,
                            highlightcolor=des.primary_color)
        buttoncanvas.place(relheight=0.9, relwidth=0.1, relx=0.9, rely=0.1)

        newbutton = Button(buttoncanvas, des.buttonconfig, text='+ NEW', command=mn.makenew)
        newbutton.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.04)
        
        
        def displayinfo():
            selection = table.selection()
            if selection:
                item = selection[0]
                values = table.item(item, "values")
                sh.passwordUI(values)
                

        
        showbutton = Button(buttoncanvas, des.buttonconfig, text='Show', command=displayinfo)
        showbutton.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.28)
        
        
        def calldelete():
            selection = table.selection()
            print(selection)
            if selection:
                rowvalues = table.item(selection[0], 'values')
                dlt.deleterow(rowvalues)

                
        
        delbutton = Button(buttoncanvas, des.buttonconfig, text='DELETE', command=calldelete)
        delbutton.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.52)
        
        
        def refresh():
            root.destroy()
            mainfunc()
        
        
        refbutton = Button(buttoncanvas, des.buttonconfig, text='Refresh', command=refresh)
        refbutton.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.76)
    #------------------------------------END OF MAIN CANVAS----------------------------------------
    
    
    def password():

        
        def submitcomm():
            
            loginpass = '123'
            
            
            if passentry.get() == conpassentry.get() == loginpass:
                passconlabel.destroy()
                passlabel.destroy()
                passentry.destroy()
                conpassentry.destroy()
                submitbutton.destroy()
                
                tablefunc()

        
        passlabel = Label(maincanvas, text="Password", bg=des.primary_color, fg='white', font=('Helvetica', 15))
        
        passlabel.grid(row=0, column=0, padx=50,pady=50)
        
        passconlabel = Label(maincanvas, text="Confirm\nPassword", bg=des.primary_color, fg='white', font=('Helvetica', 15))
        passconlabel.grid(row=1, column=0, padx=50)
        
        passentry = Entry(maincanvas, width=40, show='*', font=('Helvetica', 15))
        passentry.grid(row=0, column=1,pady=50)
        
        conpassentry = Entry(maincanvas, width=40, show='*', font=('Helvetica', 15))
        conpassentry.grid(row=1, column=1)
        
        submitbutton = Button(maincanvas, des.buttonconfig, text="Submit", command=submitcomm, font=('Helvetica', 12))
        submitbutton.place(relheight=0.1, relwidth=0.6, relx=0.2, rely=0.8)
    
    
    
    
    
    password()
    root.mainloop()
    
mainfunc()