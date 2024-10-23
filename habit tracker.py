import tkinter as tk
from tkinter import messagebox
import time
import json
import os


HABIT_FILE = 'habits_data.json'
CHECK_INTERVAL = 24 * 60 * 60  

habits = []


def load_habits():
    if os.path.exists(HABIT_FILE):
        with open(HABIT_FILE, 'r') as f:
            loaded_habits = json.load(f)
            for habit in loaded_habits:
                if 'streak' not in habit:
                    habit['streak'] = 0
                if 'completed' not in habit:
                    habit['completed'] = False
                if 'last_checked' not in habit:
                    habit['last_checked'] = 0
            return loaded_habits
    return []


def save_habits():
    with open(HABIT_FILE, 'w') as f:
        json.dump(habits, f)


def update_habit_list():
    for widget in habit_list_frame.winfo_children():
        widget.destroy()

    for index, habit in enumerate(habits):
        var = tk.BooleanVar(value=habit.get('completed', False))  
        streak = habit.get('streak', 0)  
        checkbox = tk.Checkbutton(habit_list_frame, text=f"{habit['name']} (Streak: {streak})", variable=var,
                                  command=lambda idx=index: toggle_habit(idx))
        checkbox.pack(anchor='w')

        delete_button = tk.Button(habit_list_frame, text="Delete", command=lambda idx=index: delete_habit(idx))
        delete_button.pack(anchor='w')


def toggle_habit(index):
    current_time = time.time()
    habit = habits[index]
    last_checked = habit.get('last_checked', 0)
    
    
    if current_time - last_checked >= CHECK_INTERVAL:
        habit['completed'] = not habit['completed']
        habit['last_checked'] = current_time
        if habit['completed']:
            habit['streak'] += 1
        else:
            habit['streak'] = 0
        save_habits()
        update_habit_list()


def delete_habit(index):
    del habits[index]
    save_habits()
    update_habit_list()


def add_habit():
    habit_name = habit_entry.get()
    if habit_name:
        habits.append({'name': habit_name, 'streak': 0, 'completed': False, 'last_checked': 0})
        habit_entry.delete(0, tk.END)
        save_habits()
        update_habit_list()


def reset_streaks():
    for habit in habits:
        habit['streak'] = 0
    save_habits()
    update_habit_list()


root = tk.Tk()
root.title("Habit Tracker")
root.geometry("925x500")

habit_label = tk.Label(root, text="Enter a habit to track:",font=("Microsoft YaHei UI Light", 14, "italic"), fg="#57a1f8")
habit_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

habit_entry = tk.Entry(root, width=30,font=("Microsoft YaHei UI Light", 12))
habit_entry.grid(row=3, column=1, padx=20, pady=5)

submit_button = tk.Button(root, text="Add Habit", command=add_habit,font=("Microsoft YaHei UI Light", 12), fg="#57a1f8")
submit_button.grid(row=4, column=1, padx=10)


habit_list_frame = tk.Frame(root)
habit_list_frame.grid(row=2, column=0, pady=20)


reset_button = tk.Button(root, text="Reset Streaks", command=reset_streaks,font=("Microsoft YaHei UI Light", 12), fg="#57a1f8")
reset_button.grid(row=8, column=1, pady=20)


habits = load_habits()
update_habit_list()

root.mainloop()
