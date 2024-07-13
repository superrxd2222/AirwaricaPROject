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