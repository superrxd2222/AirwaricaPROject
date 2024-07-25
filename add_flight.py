import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
import datetime

class AddFlightPage:
    def __init__(self, root):
        self.root = root
        self.root.title('Add Flight')
        self.root.geometry("1920x1080")
        self.root.state('zoomed')  # Make the window full screen

        # Connect to the database
        self.conn = sqlite3.connect('flights.db')
        self.c = self.conn.cursor()

        # Create table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS flights
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, flight_number TEXT, origin TEXT, 
                         destination TEXT, departure_date TEXT, return_date TEXT, price REAL)''')
        self.conn.commit()

        # Create main layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        # Create sidebar
        self.sidebar = tk.Frame(self.main_frame, bg='lightgray', width=200, height=1080, relief='sunken')
        self.sidebar.pack(side='left', fill='y')

        # Create sidebar buttons
        self.dashboard_button = ttk.Button(self.sidebar, text="Dashboard", command=self.open_dashboard_page)
        self.dashboard_button.pack(pady=10, padx=10, fill='x')

        self.add_flight_button = ttk.Button(self.sidebar, text="Log out", command=self.login_page)
        self.add_flight_button.pack(pady=10, padx=10, fill='x')

        # Create content frame on the left
        self.content_frame = tk.Frame(self.main_frame, bg='white', width=800)
        self.content_frame.pack(side='left', fill='both', expand=True)

        # Create image frame on the right
        self.image_frame = tk.Frame(self.main_frame, bg='white')
        self.image_frame.pack(side='right', fill='both', expand=True)

        # Load and display image
        self.load_image()

        # Add flight form
        self.create_add_flight_form()

def load_image(self):
        # Load an image
        self.image = Image.open('Airlines-min.png')
        self.image = self.image.resize((600, 400), Image.LANCZOS)  # Resize the image
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a label in the image frame
        self.image_label = tk.Label(self.image_frame, image=self.photo)
        self.image_label.pack(pady=20)

    def create_add_flight_form(self):
        tk.Label(self.content_frame, text='Add Flight', font=('Arial', 20)).pack(pady=(50, 20))  # Add more vertical space at the top

        # Create labels and entry fields with vertical padding
        tk.Label(self.content_frame, text='Flight Number').pack(pady=(10, 5))
        self.flight_number_entry = tk.Entry(self.content_frame)
        self.flight_number_entry.pack(pady=(5, 15))

        tk.Label(self.content_frame, text='Origin').pack(pady=(10, 5))
        self.origin_entry = tk.Entry(self.content_frame)
        self.origin_entry.pack(pady=(5, 15))

        tk.Label(self.content_frame, text='Destination').pack(pady=(10, 5))
        self.destination_entry = tk.Entry(self.content_frame)
        self.destination_entry.pack(pady=(5, 15))

        tk.Label(self.content_frame, text='Departure Date (YYYY-MM-DD)').pack(pady=(10, 5))
        self.departure_date_entry = tk.Entry(self.content_frame)
        self.departure_date_entry.pack(pady=(5, 15))

        tk.Label(self.content_frame, text='Return Date (YYYY-MM-DD)').pack(pady=(10, 5))
        self.return_date_entry = tk.Entry(self.content_frame)
        self.return_date_entry.pack(pady=(5, 15))

        tk.Label(self.content_frame, text='Price').pack(pady=(10, 5))
        self.price_entry = tk.Entry(self.content_frame)
        self.price_entry.pack(pady=(5, 20))

        self.save_button = tk.Button(self.content_frame, text='Save Flight', command=self.save_flight)
        self.save_button.pack(pady=30)  # Add more padding at the bottom

    def save_flight(self):
        flight_number = self.flight_number_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        departure_date = self.departure_date_entry.get()
        return_date = self.return_date_entry.get()
        try:
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Price must be a number')
            return

        # Handle empty fields
        if not flight_number or not origin or not destination or not departure_date or not return_date:
            messagebox.showerror("Error", "Please fill all fields")
            return

        # Validate date format
        try:
            datetime.datetime.strptime(departure_date, '%Y-%m-%d')
            datetime.datetime.strptime(return_date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD")
            return

        # Insert the data into the database
        self.c.execute('''
            INSERT INTO flights (flight_number, origin, destination, departure_date, return_date, price)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (flight_number, origin, destination, departure_date, return_date, price))
        self.conn.commit()

        # Clear the input fields
        self.flight_number_entry.delete(0, tk.END)
        self.origin_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.departure_date_entry.delete(0, tk.END)
        self.return_date_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        
        # Show a confirmation message
        messagebox.showinfo("Success", "Flight information saved successfully")

        def open_dashboard_page(self):
        self.root.destroy()
        import dashboard

    def login_page(self):
        self.root.destroy()
        import login

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

# Create the main window
root = tk.Tk()
app = AddFlightPage(root)
root.mainloop()
    