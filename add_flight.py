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

    