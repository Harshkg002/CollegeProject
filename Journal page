import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Journal Application")
        self.root.geometry("925x500")
        self.root.configure(bg="white")

    
        self.text_area = tk.Text(root, wrap=tk.WORD, height=15, width=50)
        self.text_area.pack(pady=10)

        
        self.save_button = tk.Button(root, text="Save Entry", command=self.save_entry)
        self.save_button.pack(pady=5)

        
        self.load_button = tk.Button(root, text="Load Entries", command=self.load_entries)
        self.load_button.pack(pady=5)

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
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()
