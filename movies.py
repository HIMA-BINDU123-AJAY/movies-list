import tkinter as tk
from tkinter import messagebox

# Ticket prices for different movies
ticket_prices = {
    "Inception": 150,
    "Avengers: Endgame": 180,
    "RRR": 200,
    "KGF": 170,
    "Leo": 160
}

def calculate_total():
    movie = movie_var.get()
    try:
        tickets = int(ticket_entry.get())
        if tickets <= 0:
            raise ValueError
        price = ticket_prices[movie]
        total = tickets * price
        total_label.config(text=f"Total Price: ₹{total}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of tickets.")

def book_ticket():
    movie = movie_var.get()
    tickets = ticket_entry.get()
    if not tickets.isdigit() or int(tickets) <= 0:
        messagebox.showerror("Error", "Please enter a valid ticket number.")
        return
    messagebox.showinfo("Booking Confirmed", f"You have successfully booked {tickets} ticket(s) for {movie}!")
    ticket_entry.delete(0, tk.END)
    total_label.config(text="Total Price: ₹0")

# GUI Setup
root = tk.Tk()
root.title("Movie Ticket Booking System")
root.geometry("400x300")
root.config(bg="#f5f5f5")

# Movie Selection
tk.Label(root, text="Select Movie:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
movie_var = tk.StringVar(root)
movie_var.set("Inception")  # default value
tk.OptionMenu(root, movie_var, *ticket_prices.keys()).pack()

# Ticket Entry
tk.Label(root, text="Number of Tickets:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
ticket_entry = tk.Entry(root)
ticket_entry.pack()

# Buttons
tk.Button(root, text="Calculate Total", command=calculate_total, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(pady=10)
total_label = tk.Label(root, text="Total Price: ₹0", font=("Arial", 12), bg="#f5f5f5")
total_label.pack()

tk.Button(root, text="Book Ticket", command=book_ticket, bg="#2196F3", fg="white", font=("Arial", 10)).pack(pady=10)

root.mainloop()
