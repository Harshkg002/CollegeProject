from tkinter import *
from devtools import find_file 
from journalpg import JournalApp
from notifierpy import Reminder
from habit_tracker import HabitTracker

class Homepage:
    def __init__(self):
        self.root = Tk()
        self.root.title("DegreeBee")
        self.root.geometry('925x500')

        bg_photo = PhotoImage(file=find_file("homepage.png"))
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="                 DegreeBee", font=("Microsoft YaHei UI Light", 24, "bold"), bg="#57a1f8")
        title.pack(pady=5)
        menu = Label(self.root, text="Home", font=("Microsoft YaHei UI Light", 24, "bold"), bg="#66a8f7")
        menu.place(x=35, y=4)
        sidebar = Frame(self.root, bg="#66a8f7", width=170, height=430)
        sidebar.pack(side=LEFT)
        sidebar.pack_propagate(False)

        self.buttons = []  # Make buttons an instance variable

        # Create the button under 'Home'
        button1 = Button(sidebar, text="Journal", bg="#66a8f7", fg="black", font=("Microsoft YaHei UI Light", 16), relief=FLAT, width=20,
                         command=self.show_journal)  # Use self to call the method
        button1.pack(pady=2)
        self.buttons.append(button1)

        button2 = Button(sidebar, text="Notifier", bg="#66a8f7", fg="black", font=("Microsoft YaHei UI Light", 16), relief=FLAT, width=20,
                         command=self.show_notifier)
        button2.pack(pady=2)
        self.buttons.append(button2)

        button3 = Button(sidebar, text="Habit tracker", bg="#66a8f7", fg="black", font=("Microsoft YaHei UI Light", 16), relief=FLAT, width=20,
                         command=self.show_habit)
        button3.pack(pady=2)
        self.buttons.append(button3)

        # Create a content frame for the main (white) area and make it an instance variable
        self.content_frame = Frame(self.root, bg="#00cbff",width=700,height=500)
        self.content_frame.pack()
        self.content_frame.pack_propagate(0)


        self.show_default()
        self.root.mainloop()
    def show_default(self):
        # Clear any existing content in the frame
        self.clear_content_frame()
        self.show_journal()
        
    def clear_content_frame(self):
        # Clear all widgets in the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def highlight_button(self, selected):
        # Reset the background of all buttons
        for button in self.buttons:
            button.config(bg="#66a8f7", relief=FLAT)

        # Highlight the selected button
        selected.config(bg="light blue", relief=GROOVE)

    def show_journal(self):
        self.clear_content_frame()  # Clear any previous content
        self.highlight_button(self.buttons[0])  # Highlight the first button
        # Display JournalApp in the content_frame
        journal_app = JournalApp(self.content_frame)

    def show_notifier(self):
        self.clear_content_frame()  # Clear any previous content
        self.highlight_button(self.buttons[1])  # Highlight the second button
        # Display NotifierApp in the content_frame
        notifier_app = Reminder(self.content_frame)
        self.content_frame.config(width=700,height=400) # Clear any previous content
        
    def show_habit(self):
        self.clear_content_frame()  # Clear any previous content
        self.highlight_button(self.buttons[2])  # Highlight the third button
        # Display habit tracker in the content_frame
        habit_app = HabitTracker(self.content_frame)

s = Homepage()
