from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Member")
        self.resizable(False,False)

        ################ FRAMES ###################################

        ## TOP Frame
        self.topFrame=Frame(self,height=150,bg='white')
        self.topFrame.pack(fill=X)
        ## BOTTOM Frame
        self.bottomFrame=Frame(self,height=600,bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        ## heading,image
        self.top_image=PhotoImage(file='addmem_2ndp.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading=Label(self.topFrame,text=' ADD Member ',font='arial 22  bold',fg='#003f8a',bg='white')
        heading.place(x=290,y=60)

        ##################### ENTRIES AND LABEL  ####################################3
        ## name
        self.label_name=Label(self.bottomFrame,text='Name :',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,'Please enter the member name')
        self.ent_name.place(x=150,y=45)
        ## phone no
        self.label_phone=Label(self.bottomFrame,text='Phone:',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_phone.place(x=40,y=80)
        self.ent_phone=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_phone.insert(0,'Please enter the Phone no')
        self.ent_phone.place(x=150,y=85)

        ## BUTTON
        button=Button(self.bottomFrame,text='ADD MEMBER',command=self.addMember)
        button.place(x=270,y=120)

    def addMember(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()


        if ( name and phone != ""):
            try:
                query = "INSERT INTO 'members' (member_name, member_phone) VALUES (?, ?)"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon='info')
            except Exception as e:
                messagebox.showerror("Error", f"Can't add to database: {e}", icon='warning')

        else:
            messagebox.showerror("Error", "Fields can't be empty", icon='warning')

