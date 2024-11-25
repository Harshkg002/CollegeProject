import tkinter as tk
from tkinter import font
from devtools import *

class Personalisation:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Page Target Selection")
        self.root.geometry("925x500")
        self.root.configure(bg="white")  # Set the background color to white

        window_width = 925
        window_height = 500
        center_window(self.root, window_width, window_height)

        # Set a custom font
        self.title_font = font.Font(family="Microsoft YaHei UI Light", size=16, weight="bold")
        self.button_font = font.Font(family="Microsoft YaHei UI Light", size=12, weight="bold")
        self.subtitle_font = font.Font(family="Microsoft YaHei UI Light", size=10)

        # Create a frame to hold the custom progress bar
        self.progress_frame = tk.Frame(self.root, bg="white")
        self.progress_frame.place(x=400, y=10)  # Position it at the top center

        # Create labels for each step to represent the segmented progress bar
        self.progress_steps = []
        for i in range(4):
            step_label = tk.Label(
                self.progress_frame,
                text=" ",
                width=15,
                height=1,
                bg="#e0e0e0" if i > 0 else "#1e88e5",  # First step filled by default
            )
            step_label.grid(row=0, column=i, padx=(0 if i == 0 else 5, 0))  # Add space between segments
            self.progress_steps.append(step_label)

        # Create a frame to hold pages
        self.pages = []

        # Text content for each page
        self.page_texts = [
            ("What's your target?", "Help us understand your needs better"),
            ("Choose your focus area", "Select what matters most to you"),
            ("Personalize your experience", "Tailor your goals for better results"),
            ("You're almost there!", "Review and confirm your selections"),
        ]

        # Define button options for each page
        self.button_texts_pages = [
            [("Live healthier", "❤️"), ("Relieve pressure", "🧘"), ("Try new things", "🌱"), ("Be more focused", "🎯"), ("Better relationship", "👥"), ("Sleep better", "🌙")],
            [("Improve diet", "🍎"), ("Exercise more", "🏋️"), ("Reduce stress", "🧘"), ("Increase energy", "⚡"), ("Better focus", "🎯"), ("Enhance sleep", "🌙")],
            [("Boost confidence", "💪"), ("Learn new skills", "📚"), ("Be more social", "👥"), ("Strengthen bonds", "❤️"), ("Feel happier", "😊"), ("Be productive", "📈")],
            [("Finalize goals", "✔️"), ("Set reminders", "⏰"), ("Track progress", "📊"), ("Stay motivated", "💪"), ("Celebrate wins", "🎉"), ("Achieve balance", "⚖️")]
        ]

        # Create four pages with unique titles, subtitles, and button texts
        for i, (title, subtitle) in enumerate(self.page_texts):
            self.create_page(title, subtitle, self.button_texts_pages[i], is_last_page=(i == 3))

        # Show the first page initially
        self.show_page(0)

    # Function to update the progress steps as each page is shown
    def update_progress(self, page_index):
        for i, step_label in enumerate(self.progress_steps):
            step_label.config(bg="#1e88e5" if i <= page_index else "#e0e0e0")

    # Function to show a specific page and update progress
    def show_page(self, page_index):
        for page in self.pages:
            page.place_forget()  # Hide all pages
        self.pages[page_index].place(relx=0.7, rely=0.1, anchor="n")  # Position closer to the right side
        self.update_progress(page_index)

    # Function to toggle button selection state
    def toggle_button(self, button):
        current_bg = button.cget("bg")
        if current_bg == "#1e88e5":  # If selected
            button.configure(
                bg="#e0e0e0",
                activebackground="#1e88e5",
                fg="black",
                activeforeground="white"
            )
        else:  # If not selected
            button.configure(
                bg="#1e88e5",
                activebackground="#1e88e5",
                fg="white",
                activeforeground="white"
            )

    # Create a function to populate each page with unique layout
    def create_page(self, title, subtitle, button_texts, is_last_page=False):
        page = tk.Frame(self.root, bg="white", width=600, height=400)
        self.pages.append(page)

        # Title and subtitle aligned below the progress bar
        title_label = tk.Label(page, text=title, fg="black", bg="white", font=self.title_font, anchor="center")
        title_label.pack(pady=(10, 5))

        subtitle_label = tk.Label(page, text=subtitle, fg="gray", bg="white", font=self.subtitle_font, anchor="center")
        subtitle_label.pack(pady=(0, 20))

        # Button frame to hold option buttons
        button_frame = tk.Frame(page, bg="white")
        button_frame.pack(pady=(0, 20))

        # Add buttons to the button frame (2 columns and 3 rows)
        for text, icon in button_texts:
            button = tk.Button(
                button_frame, 
                text=f"{icon} {text}", 
                font=self.button_font,
                fg="black", 
                bg="#e0e0e0", 
                activebackground="#1e88e5", 
                activeforeground="white",
                width=20, 
                height=2, 
                bd=0,
                relief="flat"  # Make buttons flat
            )
            
            # Use a lambda function to correctly capture the button instance
            button.config(command=lambda b=button: self.toggle_button(b))
            
            row = len(button_frame.grid_slaves()) // 2  # Determines the row (0, 1, 2)
            col = len(button_frame.grid_slaves()) % 2   # Determines the column (0, 1)
            
            button.grid(row=row, column=col, padx=10, pady=10)

        # Navigation buttons aligned below the options
        nav_frame = tk.Frame(page, bg="white")
        nav_frame.pack(pady=(20, 0))

        if not is_last_page:
            next_button = tk.Button(nav_frame, text="NEXT", font=self.button_font, fg="black", bg="#57a1f8", width=7, height=2, bd=0, command=lambda idx=len(self.pages): self.show_page(idx))
            next_button.pack()
        else:
            finish_button = tk.Button(nav_frame, text="FINISH", font=self.button_font, fg="black", bg="#57a1f8", width=7, height=2, bd=0, command=self.homepage)
            finish_button.pack()

    def homepage(self):
        import homepg as h
        self.root.destroy()
        obj=h.Homepage()

# Initialize the main window and run the application
#if __name__ == "__main__":
    #root = tk.Tk()
    #app = Personalisation(root)
    #root.mainloop()