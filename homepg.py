from tkinter import *

def highlight_button(selected):
    # Reset the background of all buttons
    for button in buttons:
        button.config(bg="#68acf4",relief=FLAT)
    
    # Highlight the selected button
    selected.config(bg="lightblue",relief=GROOVE)
    
root = Tk()
root.title("DegreeBee")
root.geometry('925x500')

bg_photo = PhotoImage(file=r"D:\python\courseBee\homepage.png")
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = Label(root, text="DegreeBee", font=("Roboto", 24), bg="#57a1f8")
label.pack(pady=7)
sidebar = Frame(root, bg="#68acf4",width=170,height=430)
sidebar.pack(side=LEFT)
sidebar.pack_propagate(False) 

buttons = []

# Create the button under 'Home'
button1 = Button(sidebar, text="Journal", bg="#68acf4", fg="black", font=("Roboto", 18),relief=FLAT, width=20,
                 command=lambda: highlight_button(button1))
button1.pack(pady=2)
buttons.append(button1)

button2 = Button(sidebar, text="Feature 2", bg="#68acf4", fg="black", font=("Roboto", 18),relief=FLAT, width=20,
                 command=lambda: highlight_button(button2))
button2.pack(pady=2)
buttons.append(button2)

button3 = Button(sidebar, text="Feature 3", bg="#68acf4", fg="black", font=("Roboto", 18),relief=FLAT, width=20,
                 command=lambda: highlight_button(button3))
button3.pack(pady=2)
buttons.append(button3)

# Create a content frame for the main (white) area
content_frame = Frame(root, bg="white")
content_frame.pack(expand=True)

# Add a label or content to show it's related to the "Open Feature"
content_label = Label(content_frame, text="You have opened the feature!", font=("Roboto", 24), bg="white")
content_label.pack(pady=20)
root.mainloop()