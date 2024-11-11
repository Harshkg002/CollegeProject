import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class JournalApp:
    def __init__(self, parent=None):
        self.window = tk.Tk() if parent is None else parent

        # Set the background color and window size
        self.parent.configure(bg="#d9f1f1")  # Change to your desired color
        # Set the text area with custom background and font
        self.text_area = tk.Text(parent, wrap=tk.WORD, height=13, width=50, bg="#ffffff",highlightbackground="grey",highlightcolor="#57a1f8",highlightthickness=4, font=("Arial", 16))
        self.text_area.pack(pady=15)
        self.text_area.insert("1.0", "Enter your text here...")

        # Save Entry Button
        self.save_button = tk.Button(parent, text="Save Entry", command=self.save_entry, bg="#4682b4", fg="white", font=("Arial", 10, "bold"))
        self.save_button.place(x=250,y=350)

        # Load Entries Button
        self.load_button = tk.Button(parent, text="Load Entries", command=self.load_entries, bg="#4682b4", fg="white", font=("Arial", 10, "bold"))
        self.load_button.place(x=400,y=350)

    def save_entry(self):
        entry = self.text_area.get("1.0", tk.END).strip()
        if entry:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("journal.txt", "a") as file:
                file.write(f"{timestamp}\n{entry}\n\n")
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Entry saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please write something before saving.")

    def load_entries(self):
        try:
            with open("journal.txt", "r") as file:
                entries = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, entries)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No entries found. Please save an entry first.")

if __name__ == "__main__":
    parent = tk.Tk()
    app = JournalApp(parent)
    parent.mainloop()