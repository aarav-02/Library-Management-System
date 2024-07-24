from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()

import addBOOK


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False,False)

        ################ FRAMES ###################################

        ## TOP Frame
        self.topFrame=Frame(self,height=150,bg='white')
        self.topFrame.pack(fill=X)
        ## BOTTOM Frame
        self.bottomFrame=Frame(self,height=600,bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        ## heading,image
        self.top_image=PhotoImage(file='addbooks_2.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading=Label(self.topFrame,text=' ADD BOOK ',font='arial 14 bold',fg='#003f8a',bg='white')
        heading.place(x=290,y=60)

        ##################### ENTRIES AND LABEL  ####################################3
        ## name
        self.label_name=Label(self.bottomFrame,text='Name :',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,'Please enter the book name')
        self.ent_name.place(x=150,y=45)
        ## author name
        self.label_author=Label(self.bottomFrame,text='Author :',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_author.place(x=40,y=80)
        self.ent_author=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_author.insert(0,'Please enter the author name')
        self.ent_author.place(x=150,y=85)
        ## page size
        self.label_page=Label(self.bottomFrame,text='Page size :',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_page.place(x=40,y=120)
        self.ent_page=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_page.insert(0,'Please enter the page size of book')
        self.ent_page.place(x=150,y=125)
        ##language
        self.label_language=Label(self.bottomFrame,text='Language:',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_language.place(x=40,y=160)
        self.ent_language=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_language.insert(0,'Please enter the language of the BOOK:')
        self.ent_language.place(x=150,y=165)
        ## BUTTON
        button=Button(self.bottomFrame,text='ADD BOOK',command=self.addBook)
        button.place(x=270,y=200)

    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if ( name != "" and author != "" and page != "" and language != ""):
            try:
                query = "INSERT INTO 'books' (book_name, book_author, book_page, book_language) VALUES (?, ?, ?, ?)"
                cur.execute(query, (name, author, page, language))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon='info')
            except Exception as e:
                messagebox.showerror("Error", f"Can't add to database: {e}", icon='warning')

        else:
            messagebox.showerror("Error", "Fields can't be empty", icon='warning')









