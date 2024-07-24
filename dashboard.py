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
