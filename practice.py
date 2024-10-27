from tkinter import *
from devtools import *

class Homepage:
    def __init__(self):
        self.root = Tk()
        self.root.title("DegreeBee")
        self.root.geometry('925x500')
        
        self.window_width = 925
        self.window_height = 500
        center_window(self.root, self.window_width, self.window_height)

        self.bg_photo = PhotoImage(file=find_file("homepage.png"))
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = Label(self.root, text="DegreeBee", font=("Roboto", 24), bg="#57a1f8")
        self.label.pack(pady=7)
        
        self.sidebar = Frame(self.root, bg="#68acf4", width=170, height=430)
        self.sidebar.pack(side=LEFT)
        self.sidebar.pack_propagate(False)

        self.buttons = []  # Make buttons an instance variable

        # Create the button under 'Home'
        self.button1 = Button(self.sidebar, text="Journal", bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                              command=lambda: self.highlight_button(self.button1))  # Use self to call the method
        self.button1.pack(pady=2)
        self.buttons.append(self.button1)

        self.button2 = Button(self.sidebar, text="Feature 2", bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                              command=lambda: self.highlight_button(self.button2))
        self.button2.pack(pady=2)
        self.buttons.append(self.button2)

        self.button3 = Button(self.sidebar, text="Feature 3", bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                              command=lambda: self.highlight_button(self.button3))
        self.button3.pack(pady=2)
        self.buttons.append(self.button3)

        # Create a content frame for the main (white) area
        self.content_frame = Frame(self.root, bg="white")
        self.content_frame.pack(expand=True)

        # Add a label or content to show it's related to the "Open Feature"
        self.content_label = Label(self.content_frame, text="You have opened the feature!", font=("Roboto", 24), bg="white")
        self.content_label.pack(pady=20)

        self.root.mainloop()

    def highlight_button(self, selected):
        # Reset the background of all buttons
        self.button1.config(bg="yellow")
    
        # Import the JournalApp class correctly
        from journalpg import JournalApp  # Correct import statement
        obj = JournalApp(self.root)

s = Homepage()