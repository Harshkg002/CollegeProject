from tkinter import *
from plyer import notification
from tkinter import messagebox
import time
from datetime import datetime, timedelta
from devtools import find_file

t = Tk()
t.title('Notifier')
t.geometry("735x440")

# Get details function
def get_details():
    get_title = title.get()
    get_msg = msg.get()

    if get_title.strip() == "" or get_msg.strip() == "":
        messagebox.showerror("Alert", "Title and message are required!")
        return

    # Specific time mode
    get_hour = time_hour.get()
    get_minute = time_minute.get()
    get_ampm = time_ampm.get()

    if get_hour.strip() == "" or get_minute.strip() == "" or get_ampm.strip() == "":
        messagebox.showerror("Alert", "Please fill in all fields for specific time!")
        return

    try:
        set_time_str = f"{get_hour}:{get_minute} {get_ampm.upper()}"
        set_time = datetime.strptime(set_time_str, "%I:%M %p").time()
        now = datetime.now()

        # Calculate time difference
        current_time = now.time()
        if set_time < current_time:
            target_time = datetime.combine(now.date(), set_time) + timedelta(days=1)
        else:
            target_time = datetime.combine(now.date(), set_time)

        time_diff = (target_time - now).total_seconds()
        messagebox.showinfo("Notifier set", f"Notification set for {set_time_str}!")
        t.destroy()
        time.sleep(time_diff)

        notification.notify(
            title=get_title,
            message=get_msg,
            app_name="Notifier",
            app_icon=find_file("icon.ico"),  # Update the path to your icon
            toast=True,
            timeout=10
        )
    except ValueError:
        messagebox.showerror("Alert", "Invalid time entered!")

# Styling constants
label_font = ("poppins", 12)
entry_font = ("poppins", 13)
button_font = ("poppins", 12, "bold")

# Center the layout - Label and Entry positions
x_label_offset = 250
x_entry_offset = 400

# Label - Title
t_label = Label(t, text="Title: ", fg="black", font=("Microsoft YaHei UI Light",16))
t_label.place(x=200, y=150)

# ENTRY - Title
title = Entry(t, width="30", fg="#57a1f8", font=entry_font)
title.place(x=350, y=150)

# Label - Message
m_label = Label(t, text="Description: ", fg="black", font=("Microsoft YaHei UI Light",16))
m_label.place(x=200, y=200)

# ENTRY - Message
msg = Entry(t, width="30", fg="#57a1f8", font=entry_font)
msg.place(x=350, height=30, y=200)

# Specific Time Mode
# Label - Time Hour
time_hour_label = Label(t, text="Hr", fg="black", font=("Microsoft YaHei UI Light",10))
time_hour_label.place(x=400, y=260)

# ENTRY - Hour (Specific Time)
time_hour = Entry(t, width="5", fg="#57a1f8", font=entry_font)
time_hour.place(x=350, y=260)

# Label - Time Minute
time_minute_label = Label(t, text="Min", fg="black", font=("Microsoft YaHei UI Light",10))
time_minute_label.place(x=500, y=260)

# ENTRY - Minute (Specific Time)
time_minute = Entry(t, width="5", fg="#57a1f8", font=entry_font)
time_minute.place(x=450, y=260)

# Label - AM/PM
ampm_label = Label(t, text="AM/PM", fg="black", font=("Microsoft YaHei UI Light",10))
ampm_label.place(x=600, y=260)

#Label - Time
t_label = Label(t, text="Time: ", fg="black", font=("Microsoft YaHei UI Light",16))
t_label.place(x=200, y=250)


# ENTRY - AM/PM
time_ampm = Entry(t, width="5", fg="#57a1f8", font=entry_font)
time_ampm.place(x=550, y=260)

# Button to set notification
but = Button(t, text="SET NOTIFICATION", font=button_font, fg="#ffffff", bg="#528DFF", width=20, relief="raised", command=get_details)
but.place(x=350, y=350)

t.resizable(0, 0)
t.mainloop()
