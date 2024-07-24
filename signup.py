from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

###created window######
root=Tk()
root.title("Sign up")
root.geometry("1920x1080")

def log_in():
    """
    Closes the  current root window and opens the login window.
    
    This function closes the current root window, typically associated with a
    signup or registration interface, and opens the login window. It achieves this
    by destroying the root  window and importing the 'login' module.

    Returns:
        None
    """
    root.destroy()
    import login
    
def connect_database():
    """
    Connects to the SQLite database and creates a table if it doesn't exist.
    
    This function connects to  the SQLite database file named 'dri.db' and creates
    a table named 'information' if it doesn't already exist. It then checks if
    the provided email already exists in the database. If the email already exists,
    it displays an error message. Otherwise, it performs various validations on
    the input fields such as ensuring all fields are filled, matching passwords,
    valid email format, valid contact number, and alphabetic first and last names.
    If all validations pass, it  inserts the new user into the database and displays
    a success message. Finally, it clears the input fields, closes the database
    connection, destroys the current root window, and imports the 'login' module
    to open the login window.

    Returns:
        None
    """
    
    conn = sqlite3.connect("dri.db")
    db = conn.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS information
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR(255),
                    firstname VARCHAR(255),
                    lastname VARCHAR(255),
                    contact INTEGER,
                    password VARCHAR(255)
                    )""")

                    # Check if the  email already exists
    email = email_entry.get()
    db.execute("SELECT * FROM information WHERE email=?", (email,))
    existing_user = db.fetchone()
    
    if existing_user:
        messagebox.showerror('Error', 'Email already exists. Please use a different email.') 
    else:
        if (email_entry.get() == '' or Firstname_entry.get() == '' or Lastname_entry.get() == '' or contact_entry.get() == '' or password_entry.get() == '' or conf_password_entry.get() == ''):
            messagebox.showerror('Error', 'All Fields Are Required.')

        elif password_entry.get() != conf_password_entry.get():
            messagebox.showerror('Error', 'Password Mismatch')
        
        elif not email_entry.get().endswith('@gmail.com'):
            messagebox.showerror('Error', 'Email must end with "@gmail.com"')
        
        elif not contact_entry.get().isdigit() or len(contact_entry.get()) != 10:
            messagebox.showerror('Error', 'Contact number must be a 10-digit integer')
        
        elif not Firstname_entry.get().isalpha(): 
            messagebox.showerror('Error', 'First name  must be alphabets.')
        
        elif not Lastname_entry.get().isalpha():
            messagebox.showerror('Error', 'last name must be alphabets.')
        
        else:
            # Insert new user if all validations pass
            firstname = Firstname_entry.get()
            lastname = Lastname_entry.get()
            contact = contact_entry.get()
            password = password_entry.get()
            db.execute("INSERT INTO information (email, firstname, lastname, contact, password) VALUES (?, ?, ?, ?, ?)", (email, firstname, lastname, contact, password))
            
            conn.commit()  
            conn.close()   

            messagebox.showinfo('Success', 'Registration Successful')
            clear()
            root.destroy() 
            import login 
            
def clear():
    """
    Clears all input fields.
    
    This function clears the content of the email, first name, last name, contact,
    password, and confirm password entry fields.

    Returns:
        None
    """
    email_entry.delete(0, 'end')
    Firstname_entry.delete(0, 'end')
    Lastname_entry.delete(0, 'end')
    contact_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    conf_password_entry.delete(0, 'end')


############Creates Sign Up  Page UI###############
    
title = Label(root,text="Already have an account?",font=("Honk",11)).place(x=1000, y=600)
Login = Button(root,text="Login",border=0,cursor='hand2',font=("Honk",11,"underline"),fg="sky blue",command=log_in).place(x=1180, y=600)

sign_up_title = Label(root,text="Sign up",font=("Cabiler",23)).place(x=1115 , y=114)
account_title = Label(root,text="Create your account",font=("cabiler",13)).place(x=1095 , y=165)

email = Label(root,text="Email*",font=("Honk",10)).place(x=1000, y=190)
email_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
email_entry.place(x=1000 , y=210,height=25)

FirstName = Label(root, text="FirstName*",font=("Honk",10)).place(x=1000, y=250)
Firstname_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
Firstname_entry.place(x=1000 , y=270,height=25)

LastName = Label(root,text="LastName*",font=("Honk",10)).place(x=1000, y=310)
Lastname_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
Lastname_entry.place(x=1000, y=330,height=25)

contact = Label(root,text="Contact No*",font=("Honk",10)).place(x=1000, y=370)
contact_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
contact_entry.place(x=1000,y=390,height=25)

Password = Label(root,text="Password*",font=("Honk",10)).place(x=1000, y=430)
password_entry = Entry(root,width=52,show='*',font=("cabiler",10,"bold"))
password_entry.place(x=1000, y=450,height=25)

conf_Password = Label(root,text="Confirm Password*",font=("Honk",10)).place(x=1000, y=490)
conf_password_entry = Entry(root,width=52,show='*',font=("cabiler",10,"bold"))
conf_password_entry.place(x=1000, y=510,height=25)

Register_button = Button(root,cursor='hand2',text="Register",width=45,border=0,fg="white",bg="sky blue", font=("Honk",10),command=connect_database).place(x=1000, y=560,height=28)

image = Image.open("Airlines-min.png")  
image = image.resize((700, 600), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label=Label(root,image=photo)
image_label.place(x=50,y=100)

root.mainloop()