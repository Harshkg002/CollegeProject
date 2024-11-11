import tkinter as tk
from tkinter import ttk, messagebox
import json
import time
import os
from typing import Dict, List, TypedDict

class Habit(TypedDict):
    id: str
    name: str
    streak: int
    completed: bool
    last_checked: float

class HabitTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Habit Tracker")
        self.window.geometry("800x600")
        self.window.config(bg="#f0f4f8")

        # Constants
        self.HABIT_FILE = "habits.json"
        self.HABIT_LIMIT = 20
        self.CHECK_INTERVAL = 24 * 60 * 60  # 24 hours in seconds
        
        # Load habits
        self.habits: List[Habit] = self.load_habits()
        
        # Setup styles
        self.setup_styles()
        
        # Setup UI
        self.setup_ui()
        
    def setup_styles(self):
        style = ttk.Style()
        
        # Configure button style with white background and custom foreground color
        style.configure(
            "White.TButton",
            background="white",
            foreground="#57a1f8",  # Change fg to #57a1f8
            borderwidth=1,
            relief="solid",
            padding=6
        )
        
        # Ensure the button background remains white in all states
        style.map(
            "White.TButton",
            background=[("active", "white"), ("pressed", "white"), ("!active", "white")],
            foreground=[("active", "#57a1f8"), ("pressed", "#57a1f8"), ("!active", "#57a1f8")],
            relief=[("pressed", "flat")]
        )
        
        # Configure checkbutton style
        style.configure("White.TCheckbutton", background="white")
        
    def setup_ui(self):
        # Title Frame
        title_frame = tk.Frame(self.window, bg="#f0f4f8")
        title_frame.pack(pady=20)
        
        title = tk.Label(
            title_frame,
            text="Habit Tracker",
            font=("Helvetica", 24, "bold"),
            fg="#1a365d",
            bg="#f0f4f8"
        )
        title.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Build better habits, one day at a time",
            font=("Helvetica", 12),
            fg="#4a5568",
            bg="#f0f4f8"
        )
        subtitle.pack(pady=5)

        # Input Frame
        input_frame = tk.Frame(self.window, bg="#f0f4f8")
        input_frame.pack(pady=20, padx=50)
        
        self.habit_entry = ttk.Entry(
            input_frame,
            font=("Helvetica", 12),
            width=40
        )
        self.habit_entry.pack(side=tk.LEFT, padx=5)
        self.habit_entry.bind("<Return>", lambda e: self.add_habit())
        
        add_button = ttk.Button(
            input_frame,
            text="Add Habit",
            command=self.add_habit,
            style="White.TButton"
        )
        add_button.pack(side=tk.LEFT, padx=5)

        # Habits List Frame
        list_frame = tk.Frame(self.window, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=(0, 20))
        
        # Create canvas and scrollbar for scrolling
        self.canvas = tk.Canvas(list_frame, bg="white")
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind mousewheel
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Update habits display
        self.update_habits_display()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def load_habits(self) -> List[Habit]:
        if os.path.exists(self.HABIT_FILE):
            with open(self.HABIT_FILE, "r") as f:
                return json.load(f)
        return []

    def save_habits(self):
        with open(self.HABIT_FILE, "w") as f:
            json.dump(self.habits, f)

    def add_habit(self):
        name = self.habit_entry.get().strip()
        if not name:
            return
            
        if len(self.habits) >= self.HABIT_LIMIT:
            messagebox.showwarning(
                "Limit Reached",
                f"You can only add up to {self.HABIT_LIMIT} habits."
            )
            return
            
        habit: Habit = {
            "id": str(int(time.time())),
            "name": name,
            "streak": 0,
            "completed": False,
            "last_checked": 0
        }
        
        self.habits.append(habit)
        self.save_habits()
        self.habit_entry.delete(0, tk.END)
        self.update_habits_display()

    def toggle_habit(self, habit: Habit):
        current_time = time.time()
        time_since_last_check = current_time - habit["last_checked"]
        
        if time_since_last_check < self.CHECK_INTERVAL:
            messagebox.showwarning(
                "Warning",
                "You can only toggle habits once every 24 hours!"
            )
            return
            
        habit["completed"] = not habit["completed"]
        habit["last_checked"] = current_time
        
        if habit["completed"]:
            habit["streak"] += 1
        else:
            habit["streak"] = 0
            
        self.save_habits()
        self.update_habits_display()

    def delete_habit(self, habit: Habit):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this habit?"):
            self.habits.remove(habit)
            self.save_habits()
            self.update_habits_display()

    def reset_streak(self, habit: Habit):
        if messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the streak?"):
            habit["streak"] = 0
            self.save_habits()
            self.update_habits_display()

    def update_habits_display(self):
        # Clear existing habits
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        if not self.habits:
            empty_label = tk.Label(
                self.scrollable_frame,
                text="No habits added yet. Start by adding a new habit above!",
                font=("Helvetica", 12),
                fg="#4a5568",
                bg="white"
            )
            empty_label.pack(pady=20)
            return

        # Add each habit
        for habit in self.habits:
            habit_frame = tk.Frame(
                self.scrollable_frame,
                bg="white",
                relief="solid",
                borderwidth=1
            )
            habit_frame.pack(fill=tk.X, padx=10, pady=5)
            
            # Left side (checkbox and name)
            left_frame = tk.Frame(habit_frame, bg="white")
            left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
            
            var = tk.BooleanVar(value=habit["completed"])
            checkbox = ttk.Checkbutton(
                left_frame,
                text=habit["name"],
                variable=var,
                command=lambda h=habit: self.toggle_habit(h),
                style="White.TCheckbutton"
            )
            checkbox.pack(side=tk.LEFT)
            
            # Right side (streak and buttons)
            right_frame = tk.Frame(habit_frame, bg="white")
            right_frame.pack(side=tk.RIGHT, padx=10)
            
            streak_label = tk.Label(
                right_frame,
                text=f"🏆 {habit['streak']}",
                font=("Helvetica", 12),
                bg="white",
                fg="#eab308"
            )
            streak_label.pack(side=tk.LEFT, padx=5)
            
            reset_button = ttk.Button(
                right_frame,
                text="↺",
                width=3,
                command=lambda h=habit: self.reset_streak(h),
                style="White.TButton"
            )
            reset_button.pack(side=tk.LEFT, padx=2)
            
            delete_button = ttk.Button(
                right_frame,
                text="×",
                width=3,
                command=lambda h=habit: self.delete_habit(h),
                style="White.TButton"
            )
            delete_button.pack(side=tk.LEFT, padx=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = HabitTracker()
    app.run()