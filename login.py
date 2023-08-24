# Imports
from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk
import tkinter as tk


# main Class
class main:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.n_username = tk.StringVar()
        self.n_password = tk.StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection

        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                       "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            msg = ""
            self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_Master.py'])

            # ================================================
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created Successfully !')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def registration(self):
        root.destroy()
        from subprocess import call
        call(["python", "heart_registration.py"])

        # mainloop(root)

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

 # , relwidth=1, relheight=1)

    # Draw Widgets
    def widgets(self):
        self.head = tk.Label(self.master, text='Welcome To Login', background="orange", font=('Times New Roman', 20),
                             pady=20)
        self.head.pack()

        # self.head.pack()
        # self.head = Label(self.master, text='LOGIN',background="gold", font=('Times New Roman', 35), pady=10)
        # self.head.pack()
        self.logf = tk.Frame(self.master, padx=50, pady=20, background="orange")
        tk.Label(self.logf, text='Username: ', background="orange", font=("Times New Roman", 20), pady=5,
                 padx=5).grid(sticky=tk.W)
        tk.Entry(self.logf, textvariable=self.username, bd=5, background="white", font=('', 15)).grid(row=0, column=1)
        tk.Label(self.logf, text='Password: ', background="orange", font=("Times New Roman", 20), pady=5,
                 padx=5).grid(sticky=tk.W)
        tk.Entry(self.logf, textvariable=self.password, bd=5, background="white", font=('', 15), show='*').grid(row=1,
                                                                                                                column=1)
        tk.Button(self.logf, text=' Login ', command=self.login, bd=2, font=("Times New Roman", 20), background="Red",
                  foreground="white", padx=2, pady=2).grid(rowspan=10,columnspan=10)
        #Button.place(x=300, y=300)

        #tk.Button(self.logf, text=' Create Account ', font=("Times New Roman", 20), background="black",
               #   foreground="white", bd=3, padx=5, pady=5, command=self.registration).grid(row=2,
                                                                                           # column=1)

        self.logf.pack()
        self.crf = tk.Frame(self.master, padx=200, pady=200)


root = tk.Tk()

root.configure(background="orange")
root.geometry("500x400")
root.title("Login")

#image2 = Image.open('logimg1.jpg')
#image2 = image2.resize((500, 500), Image.ANTIALIAS)

#background_image = ImageTk.PhotoImage(image2)

#background_label = tk.Label(root, image=background_image)

#background_label.image = background_image

#background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

main(root)

root.mainloop()
