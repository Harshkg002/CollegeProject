from PIL import Image
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import devtools


class JournalApp:
    def __init__(self, parent):
        # Embed JournalApp in the provided parent frame
        self.frame = ctk.CTkFrame(parent,fg_color="#ffffff", corner_radius=20)
        self.frame.pack( padx=10,pady=10,fill="both", expand=True)

        def clear_text(event):
            # Check if the text is the default text, and clear if it is
            if self.text_area.get("1.0", "end-1c") == "What’s been the highlight of your day?":
                self.text_area.delete("1.0", "end")

        # Create the text area
        self.text_area = ctk.CTkTextbox(
        self.frame, height=300, width=500, corner_radius=10,
        font=ctk.CTkFont(size=16, family="Arial")
        )
        self.text_area.pack(pady=15, padx=15)
        self.text_area.insert("1.0", "What's been the highlight of your day?")

        # Bind the clear_text function to the left-click event
        self.text_area.bind("<Button-1>", clear_text) 

        # Button frame
        self.button_frame = ctk.CTkFrame(self.frame,fg_color="white", corner_radius=10)
        self.button_frame.pack(pady=(10,0))

        # Save Entry Button
        self.save_button = ctk.CTkButton(
            self.button_frame, text="Save Entry",
            command=self.save_entry, corner_radius=10
        )
        self.save_button.pack(side="left", padx=10)

        # Load Entries Button
        self.load_button = ctk.CTkButton(
            self.button_frame, text="Load Entries",
            command=self.load_entries, corner_radius=10
        )
        self.load_button.pack(side="left", padx=10)
       # Create a Label to display success or warning message
        result_label = ctk.CTkLabel(self.button_frame, text="", font=("Arial", 12))
        result_label.pack() 
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