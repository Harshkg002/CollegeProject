import customtkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Reminder:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.CTkFrame(parent, fg_color="white")
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.notification_label = tk.CTkLabel(self.frame, text="", fg_color="white", text_color="#57a1f8", font=("Microsoft YaHei UI Light", 12))
        self.notification_label.pack(pady=5)

        self.main_frame = tk.CTkFrame(self.frame, fg_color="white")
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.t_label = tk.CTkLabel(self.main_frame, text="Title: ", text_color="black", font=("Roboto", 18), fg_color='white')
        self.t_label.pack(anchor="w", pady=5)

        self.title = tk.CTkEntry(self.main_frame, width=40, text_color="#57a1f8", font=("Roboto", 16), fg_color='white')
        self.title.pack(fill=tk.X, pady=5)

        self.m_label = tk.CTkLabel(self.main_frame, text="Description: ", text_color="black", font=("Roboto", 18), fg_color='white')
        self.m_label.pack(anchor="w", pady=5)

        self.msg = tk.CTkEntry(self.main_frame, width=40, text_color="#57a1f8", font=("Roboto", 16), fg_color='white')
        self.msg.pack(fill=tk.X, pady=5)

        self.time_frame = tk.CTkFrame(self.main_frame, fg_color='white')
        self.time_frame.pack(pady=10)

        self.time_hour = tk.CTkEntry(self.time_frame, width=30, text_color="#57a1f8", font=("Roboto", 16), fg_color='white')
        self.time_hour.pack(side=tk.LEFT, padx=5)
        tk.CTkLabel(self.time_frame, text=":", text_color="black", font=("Roboto", 14), fg_color='white').pack(side=tk.LEFT)

        self.time_minute = tk.CTkEntry(self.time_frame, width=30, text_color="#57a1f8", font=("Roboto", 16), fg_color='white')
        self.time_minute.pack(side=tk.LEFT, padx=5)
        tk.CTkLabel(self.time_frame, text="", text_color="black", font=("Roboto", 14), fg_color='white').pack(side=tk.LEFT)

        self.time_ampm = tk.CTkEntry(self.time_frame, width=36, text_color="#57a1f8", font=("Roboto", 16), fg_color='white')
        self.time_ampm.pack(side=tk.LEFT, padx=3)
        tk.CTkLabel(self.time_frame, text="AM/PM", text_color="black", font=("Roboto", 14), fg_color='white').pack(side=tk.LEFT)

        self.set_button = tk.CTkButton(self.main_frame, text="SET NOTIFICATION", fg_color="#57a1f8", text_color="black", font=("Roboto", 16, "bold"), command=self.get_details)
        self.set_button.pack(pady=10)

        self.reminders_label = tk.CTkLabel(self.main_frame, text="Scheduled Reminders:", text_color="black", font=("Roboto", 18), fg_color='white')
        self.reminders_label.pack(anchor="w", pady=10)

        self.reminders_text = tk.CTkTextbox(self.main_frame, wrap=tk.WORD, font=("Roboto", 14), fg_color='white', height=6)
        self.reminders_text.pack(fill=tk.BOTH, expand=True)

        for widget in [self.title, self.msg, self.time_hour, self.time_minute, self.time_ampm]:
            widget.bind("<Return>", self.focus_next)

        self.load_reminders()

    def show_notification(self, message):
        # Create a new Toplevel window for the notification pop-up
        popup = tk.CTkToplevel(self.parent)
        popup.title("Reminder Notification")
        popup.geometry("300x150")
        popup.configure(fg_color="white")

        # Display the notification message inside the pop-up window
        message_label = tk.CTkLabel(popup, text=message, fg_color="white", text_color="#57a1f8", font=("Microsoft YaHei UI Light", 12))
        message_label.pack(pady=20, padx=20)

        # Close button to dismiss the pop-up manually
        close_button = tk.CTkButton(popup, text="Close", fg_color="#57a1f8", text_color="black", command=popup.destroy)
        close_button.pack(pady=10)

        # Automatically close the pop-up after 5 seconds
        popup.after(5000, popup.destroy)

    def hide_notification(self):
        # Clear the notification label
        self.notification_label.config(text="")

    def get_details(self):
        get_title = self.title.get()
        get_msg = self.msg.get()

        if get_title.strip() == "" or get_msg.strip() == "":
            messagebox.showerror("Alert", "Title and message are required!")
            return

        get_hour = self.time_hour.get()
        get_minute = self.time_minute.get()
        get_ampm = self.time_ampm.get()

        if get_hour.strip() == "" or get_minute.strip() == "" or get_ampm.strip() == "":
            messagebox.showerror("Alert", "Please fill in all fields for specific time!")
            return

        try:
            set_time_str = f"{get_hour}:{get_minute} {get_ampm.upper()}"
            set_time = datetime.strptime(set_time_str, "%I:%M %p").time()
            now = datetime.now()

            current_time = now.time()
            if set_time < current_time:
                target_time = datetime.combine(now.date(), set_time) + timedelta(days=1)
            else:
                target_time = datetime.combine(now.date(), set_time)

            time_diff = (target_time - now).total_seconds()
            print(f"Time difference in seconds: {time_diff}")  # Debugging print

            if time_diff > 0:
                self.schedule_notification(time_diff, get_title, get_msg)
                self.save_reminder(get_title, get_msg, set_time_str)
                self.load_reminders()
                self.show_notification(f"Notification set for {set_time_str}!")
            else:
                messagebox.showerror("Alert", "Invalid time entered!")

            self.title.delete(0, tk.END)
            self.msg.delete(0, tk.END)
            self.time_hour.delete(0, tk.END)
            self.time_minute.delete(0, tk.END)
            self.time_ampm.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Alert", "Invalid time entered!")

    def schedule_notification(self, time_diff, title, message):
        print(f"Scheduling notification in {time_diff} seconds")  # Debugging print
        self.frame.after(int(time_diff * 1000), lambda: self.show_notification(f"{title}: {message}"))

    def focus_next(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def load_reminders(self):
        try:
            with open("reminders.txt", "r") as file:
                reminders = file.read()
                self.reminders_text.delete("1.0", tk.END)
                self.reminders_text.insert(tk.END, reminders)
        except FileNotFoundError:
            self.reminders_text.delete("1.0", tk.END)
            self.reminders_text.insert(tk.END, "No reminders scheduled yet.")

    def save_reminder(self, title, message, time):
        with open("reminders.txt", "a") as file:
            file.write(f"{time} - {title}: {message}\n")
        self.load_reminders()

if __name__ == "__main__":
    parent = tk.CTk()
    app = Reminder(parent)
    parent.mainloop()
