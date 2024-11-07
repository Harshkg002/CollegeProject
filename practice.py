from tkinter import *
import devtools as d
from journalpg import JournalApp
class Homepage:
    def __init__(self):
        self.root = Tk()
        self.root.title("DegreeBee")
        self.root.geometry('925x500')

        self.window_width = 925
        self.window_height = 500
        d.center_window(self.root, self.window_width, self.window_height)

        # Background image setup
        self.bg_photo = PhotoImage(file=d.find_file("homepage.png"))
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = Label(self.root, text="DegreeBee", font=("Roboto", 24), bg="#57a1f8")
        self.label.pack(pady=7)

        # Sidebar setup
        self.sidebar = Frame(self.root, bg="#68acf4", width=170, height=430)
        self.sidebar.pack(side=LEFT, fill=Y)
        self.sidebar.pack_propagate(False)

        # Buttons setup
        self.buttons = []  # Store buttons for easy access
        self.create_sidebar_buttons()

        # Content frame to display the selected feature
        self.content_frame = Frame(self.root, bg="white")
        self.content_frame.pack(expand=True, fill=BOTH)

        self.root.mainloop()

    def create_sidebar_buttons(self):
        # Helper to create sidebar buttons
        button_info = [("Journal", self.show_journal),
                       ("Feature 2", self.show_feature2),
                       ("Feature 3", self.show_feature3)]
        for text, command in button_info:
            button = Button(self.sidebar, text=text, bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                            command=command)
            button.pack(pady=2)
            self.buttons.append(button)

    def clear_content_frame(self):
        # Clear all widgets in the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def highlight_button(self, selected_button):
        # Reset all buttons' background to default and highlight the selected button
        for button in self.buttons:
            button.config(bg="#68acf4")
        selected_button.config(bg="yellow")

    def show_journal(self):
        self.clear_content_frame()  # Clear any previous content
        self.highlight_button(self.buttons[0])  # Highlight the first button
        label = Label(self.content_frame, text="Welcome to the Journal!", font=("Roboto", 24), bg="white")
        label.pack(pady=20)
        # Import and initialize JournalApp if needed
        obj = JournalApp(self.root)

    def show_feature2(self):
        self.clear_content_frame()  # Clear any previous content
        self.highlight_button(self.buttons[1])  # Highlight the second button
        label = Label(self.content_frame, text="Feature 2 is under construction!", font=("Roboto", 24), bg="white")
        label.pack(pady=20)

    def show_feature3(self):
        self.clear_content_frame()  # Clear any previous content
        self.highlight_button(self.buttons[2])  # Highlight the third button
        label = Label(self.content_frame, text="Feature 3 coming soon!", font=("Roboto", 24), bg="white")
        label.pack(pady=20)

s = Homepage()
