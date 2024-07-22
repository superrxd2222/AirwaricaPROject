from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

# Start login page
root = Tk()
root.title("Air-Warica Airline Login")
root.geometry("1980x1080")

# Load image and display it on the left
image = Image.open("Airlines-min.png")
image = image.resize((600, 400), Image.LANCZOS)  # Resize image with high-quality filter
photo = ImageTk.PhotoImage(image)
image_label = Label(root, image=photo)
image_label.place(x=50, y=150)

# Function to handle user login
def login_user():
    """
        This function attempts to  log in a user by checking if the username and password fields are not empty.
        If both fields are filled, it connects to a SQLite database, retrieves user data based on the provided
        username and password, and verifies if such a user exists. If the user exists, it displays a success
        message;  otherwise, it shows an error message indicating invalid credentials.
        
      """
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required.')
    else:
        conn = sqlite3.connect("dri.db")
        db = conn.cursor()
        
        email = username_entry.get()
        password = password_entry.get()
        
        db.execute("SELECT * FROM information WHERE email=? AND password=?", (email, password))

        user_data = db.fetchone()
        
        if user_data==None:
            messagebox.showerror('Error','Invalid username or password.')
            clear()  
        else:
            messagebox.showinfo('Welcome','Login is Successful.')
           
        
            conn.close()
            root.destroy()
            import dashboard


def clear():
    """
    Clears the content of the username and password entry fields.
    """
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


def login():
    root.destroy()
    import signup

# Login page UI
welcome = Label(root, text="Welcome to Airline Login", font=("Calibri", 23, "bold")).place(x=760, y=200)
login_in = Label(root, text="Log in to continue", font=("Calibri", 23)).place(x=760, y=250)
question = Label(root, text="Don't have an account?", font=("Calibri", 13)).place(x=760, y=300)
sign_up = Button(root, text="Create a new account", border=0, font=("Calibri", 13, "underline"), cursor='hand2', fg="sky blue", command=login).place(x=960, y=298)

username = Label(root, text="Email", font=("Calibri", 10)).place(x=760, y=350)
username_entry = Entry(root, width=52, border=4, font=("Calibri", 10, "bold"))
username_entry.place(x=760, y=380, height=35)

password = Label(root, text="Password", font=("Calibri", 10)).place(x=760, y=420)
password_entry = Entry(root, width=52, border=4, font=("Calibri", 10, "bold"), show='*')
password_entry.place(x=760, y=450, height=35)


log_in_button = Button(root, cursor='hand2', text="Log in", width=52, fg="white", bg="sky blue", font=("Calibri", 10), command=login_user)
log_in_button.place(x=760, y=500)

root.mainloop()
            

            