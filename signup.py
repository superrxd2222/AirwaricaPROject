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