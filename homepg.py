from tkinter import *
from devtools import find_file 
class Homepage:
    def __init__(self):
        self.root = Tk()
        self.root.title("DegreeBee")
        self.root.geometry('925x500')
        

        bg_photo = PhotoImage(file=find_file("homepage.png"))
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(self.root, text="DegreeBee", font=("Roboto", 24), bg="#57a1f8")
        label.pack(pady=7)
        sidebar = Frame(self.root, bg="#68acf4", width=170, height=430)
        sidebar.pack(side=LEFT)
        sidebar.pack_propagate(False)

        self.buttons = []  # Make buttons an instance variable

        # Create the button under 'Home'
        button1 = Button(sidebar, text="Journal", bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                         command=lambda: self.highlight_button(button1))  # Use self to call the method
        button1.pack(pady=2)
        self.buttons.append(button1)

        button2 = Button(sidebar, text="Feature 2", bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                         command=lambda: self.highlight_button(button2))
        button2.pack(pady=2)
        self.buttons.append(button2)

        button3 = Button(sidebar, text="Feature 3", bg="#68acf4", fg="black", font=("Roboto", 18), relief=FLAT, width=20,
                         command=lambda: self.highlight_button(button3))
        button3.pack(pady=2)
        self.buttons.append(button3)

        # Create a content frame for the main (white) area
        content_frame = Frame(self.root, bg="white")
        content_frame.pack(expand=True)

        # Add a label or content to show it's related to the "Open Feature"
        content_label = Label(content_frame, text="You have opened the feature!", font=("Roboto", 24), bg="white")
        content_label.pack(pady=20)

        self.root.mainloop()

    def highlight_button(self, selected):
        # Reset the background of all buttons
        for button in self.buttons:
            button.config(bg="#68acf4", relief=FLAT)

        # Highlight the selected button
        selected.config(bg="lightblue", relief=GROOVE)

s = Homepage()