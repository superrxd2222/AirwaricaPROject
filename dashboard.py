import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime

class BookTicketPage:
    def __init__(self, root):
        self.root = root
        self.top = tk.Toplevel(root)
        self.top.title('Book Ticket')
        self.top.geometry('400x300')

        tk.Label(self.top, text='Enter Flight ID:', font=('Arial', 14)).pack(pady=10)
        self.flight_id_entry = tk.Entry(self.top)
        self.flight_id_entry.pack(pady=5)

        tk.Button(self.top, text='Book Ticket', command=self.book_ticket).pack(pady=20)

    def book_ticket(self):
        flight_id = self.flight_id_entry.get()

        if not flight_id.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid Flight ID")
            return

        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("SELECT * FROM flights WHERE id = ?", (flight_id,))
        flight = c.fetchone()

        if not flight:
            messagebox.showerror("Error", "Flight ID not found")
            return

        # Simulate invoice creation
        invoice_text = f"Invoice\n\nFlight Number: {flight[1]}\nOrigin: {flight[2]}\nDestination: {flight[3]}\n" \
                       f"Departure Date: {flight[4]}\nReturn Date: {flight[5]}\nPrice: ${flight[6]:.2f}"
        messagebox.showinfo("Invoice", invoice_text)

        conn.close()

        class UpdateFlightPage:
    def __init__(self, root, flight_data):
        self.root = root
        self.top = tk.Toplevel(root)
        self.top.title('Update Flight')
        self.top.geometry('400x500')

        self.flight_id = flight_data[0]
        
        tk.Label(self.top, text='Update Flight', font=('Arial', 16)).pack(pady=10)

        tk.Label(self.top, text='Flight Number').pack(pady=5)
        self.flight_number_entry = tk.Entry(self.top)
        self.flight_number_entry.pack(pady=5)
        self.flight_number_entry.insert(0, flight_data[1])

        tk.Label(self.top, text='Origin').pack(pady=5)
        self.origin_entry = tk.Entry(self.top)
        self.origin_entry.pack(pady=5)
        self.origin_entry.insert(0, flight_data[2])

        tk.Label(self.top, text='Destination').pack(pady=5)
        self.destination_entry = tk.Entry(self.top)
        self.destination_entry.pack(pady=5)
        self.destination_entry.insert(0, flight_data[3])

        tk.Label(self.top, text='Departure Date (YYYY-MM-DD)').pack(pady=5)
        self.departure_date_entry = tk.Entry(self.top)
        self.departure_date_entry.pack(pady=5)
        self.departure_date_entry.insert(0, flight_data[4])

        tk.Label(self.top, text='Return Date (YYYY-MM-DD)').pack(pady=5)
        self.return_date_entry = tk.Entry(self.top)
        self.return_date_entry.pack(pady=5)
        self.return_date_entry.insert(0, flight_data[5])

        tk.Label(self.top, text='Price').pack(pady=5)
        self.price_entry = tk.Entry(self.top)
        self.price_entry.pack(pady=5)
        self.price_entry.insert(0, flight_data[6])

        tk.Button(self.top, text='Update Flight', command=self.update_flight).pack(pady=20)

    def update_flight(self):
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

        if not flight_number or not origin or not destination or not departure_date or not return_date:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            datetime.datetime.strptime(departure_date, '%Y-%m-%d')
            datetime.datetime.strptime(return_date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD")
            return

        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute('''UPDATE flights SET flight_number = ?, origin = ?, destination = ?, 
                    departure_date = ?, return_date = ?, price = ? WHERE id = ?''',
                (flight_number, origin, destination, departure_date, return_date, price, self.flight_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Flight updated successfully")

        # Close the update window
        self.top.destroy()

        # Destroy the main window and reopen the dashboard
        self.root.destroy()
        new_root = tk.Tk()
        DashboardPage(new_root)


class DashboardPage:
    def __init__(self, root):
        self.root = root
        self.root.title('Dashboard')
        self.root.geometry("1920x1080")
        self.root.state('zoomed')  # Make the window full screen

        # Connect to the database
        self.conn = sqlite3.connect('flights.db')
        self.c = self.conn.cursor()

        # Create main layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        # Create sidebar
        self.sidebar = tk.Frame(self.main_frame, bg='lightgray', width=200, height=1080, relief='sunken')
        self.sidebar.pack(side='left', fill='y')

        # Create sidebar buttons
        

        self.add_flight_button = ttk.Button(self.sidebar, text="Add Flight", command=self.open_add_flight_page)
        self.add_flight_button.pack(pady=10, padx=10, fill='x')

        self.book_ticket_button = ttk.Button(self.sidebar, text="Book Ticket", command=self.open_book_ticket_page)
        self.book_ticket_button.pack(pady=10, padx=10, fill='x')

        self.add_flight_button = ttk.Button(self.sidebar, text="Log out", command=self.login_page)
        self.add_flight_button.pack(pady=10, padx=10, fill='x')

        # Create content frame
        self.content_frame = tk.Frame(self.main_frame, bg='white')
        self.content_frame.pack(side='left', fill='both', expand=True)

        # Load flights into the dashboard
        self.load_flights()

    def load_flights(self):
        # Clear existing content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        tk.Label(self.content_frame, text='Available Flights', font=('Arial', 20)).pack(pady=10)

        self.flight_list = ttk.Treeview(self.content_frame, columns=("ID", "Flight Number", "Origin", "Destination", "Departure Date", "Return Date", "Price"), show='headings')
        self.flight_list.pack(fill='both', expand=True)

        for col in self.flight_list["columns"]:
            self.flight_list.heading(col, text=col)
        
        self.c.execute("SELECT * FROM flights")
        flights = self.c.fetchall()
        for flight in flights:
            self.flight_list.insert('', 'end', values=flight)

        # Update Flight Section
        update_frame = tk.Frame(self.content_frame, bg='white')
        update_frame.pack(fill='x', pady=10)

        tk.Label(update_frame, text='Flight ID:', bg='white').pack(side='left', padx=5)
        self.update_flight_id_entry = tk.Entry(update_frame)
        self.update_flight_id_entry.pack(side='left', padx=5)

        self.update_button = ttk.Button(update_frame, text="Update Flight", command=self.open_update_flight_page)
        self.update_button.pack(side='left', padx=10, pady=10)

        # Delete Flight Section
        delete_frame = tk.Frame(self.content_frame, bg='white')
        delete_frame.pack(fill='x', pady=10)

        tk.Label(delete_frame, text='Flight ID:', bg='white').pack(side='left', padx=5)
        self.delete_flight_id_entry = tk.Entry(delete_frame)
        self.delete_flight_id_entry.pack(side='left', padx=5)

        self.delete_button = ttk.Button(delete_frame, text="Delete Flight", command=self.delete_flight)
        self.delete_button.pack(side='left', padx=10, pady=10)

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
