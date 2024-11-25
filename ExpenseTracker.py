import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class ExpenseTracker:
    def __init__(self, parent):
        # Main frame for ExpenseTracker (customtkinter)
        self.frame = ctk.CTkFrame(parent, fg_color="white")
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Title (customtkinter)
        self.title_label = ctk.CTkLabel(
            self.frame, text="Expense Tracker", font=("Roboto", 20,"bold"), fg_color="white",text_color="black")
        self.title_label.pack(pady=10)

        # Entry for item (customtkinter)
        self.item_label = ctk.CTkLabel(self.frame, text="Item:", font=("Roboto", 16,"bold"), fg_color="white",text_color="black")
        self.item_label.place(x=210, y=55)
        self.item_entry = ctk.CTkEntry(self.frame, width=250,fg_color="#ebebeb",text_color="black")
        self.item_entry.pack(pady=5)

        # Entry for cost (customtkinter)
        self.cost_label = ctk.CTkLabel(self.frame, text="Cost:", font=("Roboto", 16,"bold"), fg_color="white",text_color="black")
        self.cost_label.place(x=210, y=95)
        self.cost_entry = ctk.CTkEntry(self.frame, width=250,fg_color="#ebebeb",text_color="black")
        self.cost_entry.pack(pady=5)

        # Button to add expense (customtkinter)
        self.add_button = ctk.CTkButton(
            self.frame, text="Add Expense", fg_color="#357ABD", text_color="white",hover_color="blue", command=self.add_expense)
        self.add_button.place(x=315, y=125)

        # Listbox to show expenses (native Tkinter Listbox)
        self.expense_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.expense_listbox.pack(pady=(50,20))

        # Label to show total expenses (customtkinter)
        self.total_label = ctk.CTkLabel(
            self.frame, text="Total: ₹0", font=("Roboto", 20), fg_color="white",text_color="black")
        self.total_label.pack()

        # List to store expenses
        self.expenses = []
        self.total_by_month = {}

    def add_expense(self):
        item = self.item_entry.get()
        cost = self.cost_entry.get()

        try:
            cost = float(cost)
            date = datetime.now().strftime("%Y-%m-%d")
            self.expenses.append((date, item, cost))
            self.update_expenses()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid cost.")

    def update_expenses(self):
        self.expense_listbox.delete(0, tk.END)  # Clear the listbox
        total = 0
        current_month = datetime.now().strftime("%Y-%m")

        for date, item, cost in self.expenses:
            month = date[:7]
            self.expense_listbox.insert(tk.END, f"{date} - {item}: ₹{cost:.2f}")
            if month not in self.total_by_month:
                self.total_by_month[month] = 0
            self.total_by_month[month] += cost
            if month == current_month:
                total += cost

        if current_month in self.total_by_month:
            self.total_label.configure(
                text=f"Total this month: ₹{self.total_by_month[current_month]:.2f}"
            )


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Expense Tracker")
    root.geometry("988x534")
    app = ExpenseTracker(root)
    root.mainloop()
