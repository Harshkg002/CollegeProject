from PIL import Image
import customtkinter as ctk
import devtools
import habit_tracker
from journalpg import JournalApp
from notifierpy import Reminder 
from ExpenseTracker import ExpenseTracker

class DegreeBeeDashboard:
    def __init__(self):
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("DegreeBee Dashboard")
        self.root.geometry("925x500")
        self.root.configure(bg="white")

        self.buttons = []
        self.right_panel = None
        self.current_feature_frame = None
        self.init_ui()
        self.root.mainloop()

    def init_ui(self):
        self.create_top_nav()
        self.create_left_panel()
        self.create_right_panel()

    def create_top_nav(self):
        top_nav = ctk.CTkFrame(self.root, height=60, fg_color="#ebebeb", corner_radius=0)
        top_nav.pack(side="top", fill="x")

        degreebee_icon = ctk.CTkImage(
            light_image=Image.open(devtools.find_file("degreebee.png")),
            size=(110, 60),
        )
        icon_label = ctk.CTkLabel(top_nav, text="", image=degreebee_icon)
        icon_label.pack(side="left")

        search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(
            top_nav,
            textvariable=search_var,
            placeholder_text="Search Colleges, Courses, or Reviews",
            width=400,
            height=35,
            fg_color="white",
        )
        search_entry.place(x=245, y=6)

        search_button = ctk.CTkButton(
            top_nav,
            text="Search",
            width=80,
            height=35,
            fg_color="#4A90E2",
            text_color="white",
            hover_color="#357ABD",
            corner_radius=100,
        )
        search_button.place(x=650, y=6)

    def create_left_panel(self):
        left_panel = ctk.CTkFrame(self.root, width=250, fg_color="#ebebeb", corner_radius=0)
        left_panel.pack(side="left", fill="y", padx=10)
        left_panel_label = ctk.CTkLabel(left_panel,text="")
        left_panel_label.pack()
        # Load Icons
        icons = {
            "Journal": "journal.png",
            "Reminders": "notification.png",
            "Habits": "habit.png",
            "Expenses": "expense.png",
        }
        for name, icon_file in icons.items():
            icon = ctk.CTkImage(
                light_image=Image.open(devtools.find_file(icon_file)),
                size=(60, 40),
            )
            button = ctk.CTkButton(
                left_panel,
                text="",
                image=icon,
                width=50,
                height=40,
                corner_radius=100,
                fg_color="transparent",
                text_color="white",
                hover_color="#357ADB",
                command=lambda feature=name: self.on_feature_click(feature),
            )
            button.pack(pady=8)
            self.buttons.append(button)

    def create_right_panel(self):
        self.right_panel = ctk.CTkFrame(self.root, corner_radius=15, fg_color="white")
        self.right_panel.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=(0, 10))
        self.current_feature_frame = JournalApp(self.right_panel).frame
        self.buttons[0].configure(fg_color="#4A90E2", text_color="white", hover_color="#4A90E2")

    def clear_right_panel(self):
        if self.current_feature_frame:
            self.current_feature_frame.destroy()
            self.current_feature_frame = None

    def on_feature_click(self, feature):
        self.clear_right_panel()
        for button in self.buttons:
            button.configure(fg_color="transparent", text_color="white", hover_color="#357ABD")

        if feature == "Journal":
            # Initialize JournalApp in the right panel
            self.current_feature_frame = JournalApp(self.right_panel).frame
            # Highlight the clicked button
            self.buttons[0].configure(fg_color="#4A90E2", text_color="white", hover_color="#4A90E2")
        elif feature == "Reminders":
            self.current_feature_frame = Reminder(self.right_panel).frame
            self.buttons[1].configure(fg_color="#4A90E2", text_color="white", hover_color="#4A90E2")
        elif feature == "Habits":
            self.current_feature_frame = habit_tracker.HabitTracker(self.right_panel).frame
            self.buttons[2].configure(fg_color="#4A90E2", text_color="white", hover_color="#4A90E2")
        elif feature == "Expenses":
            self.current_feature_frame = ExpenseTracker(self.right_panel).frame
            self.buttons[3].configure(fg_color="#4A90E2", text_color="white", hover_color="#4A90E2")
        else:
            # Display a placeholder message for other features
            self.current_feature_frame = ctk.CTkTextbox(
                self.right_panel,
                font=("Arial", 14),
                fg_color="white",
                text_color="#333333",
                height=500,
                state="normal",
                corner_radius=15,
            )
            self.current_feature_frame.pack(fill="both", expand=True, pady=10)
            self.current_feature_frame.insert("1.0", f"{feature} feature is under construction!")
            self.current_feature_frame.configure(state="disabled")


if __name__ == "__main__":
    DegreeBeeDashboard()