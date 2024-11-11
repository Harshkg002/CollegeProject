import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

ctk.set_appearance_mode("light")  # Can be "light" or "dark"
ctk.set_default_color_theme("blue")  # You can change this to other themes

class JournalApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Journal App")
        self.window.geometry("600x450")

        # Main frame
        self.frame = ctk.CTkFrame(self.window, corner_radius=20)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Text area
        self.text_area = ctk.CTkTextbox(self.frame, height=300, width=500, corner_radius=10, 
                                        font=ctk.CTkFont(size=16, family="Arial"))
        self.text_area.pack(pady=15, padx=15)
        self.text_area.insert("1.0", "Enter your text here...")

        # Button frame
        self.button_frame = ctk.CTkFrame(self.frame, corner_radius=10)
        self.button_frame.pack(pady=10)

        # Save Entry Button
        self.save_button = ctk.CTkButton(self.button_frame, text="Save Entry", 
                                         command=self.save_entry, corner_radius=10)
        self.save_button.pack(side="left", padx=10)

        # Load Entries Button
        self.load_button = ctk.CTkButton(self.button_frame, text="Load Entries", 
                                         command=self.load_entries, corner_radius=10)
        self.load_button.pack(side="left", padx=10)

    def save_entry(self):
        entry = self.text_area.get("1.0", "end-1c").strip()
        if entry:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("journal.txt", "a") as file:
                file.write(f"{timestamp}\n{entry}\n\n")
            self.text_area.delete("1.0", "end")
            messagebox.showinfo("Success", "Entry saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please write something before saving.")

    def load_entries(self):
        try:
            with open("journal.txt", "r") as file:
                entries = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", entries)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No entries found. Please save an entry first.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = JournalApp()
    app.run()
