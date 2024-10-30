import tkinter as tk
from tkinter import messagebox
import time
import json
import os

HABIT_FILE = 'habits_data.json'
CHECK_INTERVAL = 24 * 60 * 60  # 24 hours
HABIT_LIMIT = 20  # Set the maximum number of habits

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
    # Clear existing habit list display
    for widget in habit_list_frame.winfo_children():
        widget.destroy()

    # Display each habit in a grid
    for index, habit in enumerate(habits):
        streak = habit.get('streak', 0)
        completed = habit.get('completed', False)

        # Checkbox for completion status
        var = tk.BooleanVar(value=completed)
        checkbox = tk.Checkbutton(habit_list_frame, variable=var, command=lambda idx=index: toggle_habit(idx))
        checkbox.grid(row=index, column=0, padx=10, pady=5)

        # Habit name
        tk.Label(habit_list_frame, text=habit['name']).grid(row=index, column=1, padx=10, pady=5)

        # Streak count
        tk.Label(habit_list_frame, text=str(streak)).grid(row=index, column=2, padx=10, pady=5)

        # Delete button
        delete_button = tk.Button(habit_list_frame, text="Delete", command=lambda idx=index: delete_habit(idx))
        delete_button.grid(row=index, column=3, padx=10, pady=5)

        # Reset streak button
        reset_button = tk.Button(habit_list_frame, text="Reset Streak", command=lambda idx=index: reset_habit_streak(idx))
        reset_button.grid(row=index, column=4, padx=10, pady=5)

    # Update scroll region based on the number of habits
    update_scroll_region()

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
    else:
        messagebox.showwarning("Warning", "You can only toggle habits once every 24 hours!")

def delete_habit(index):
    del habits[index]
    save_habits()
    update_habit_list()

def add_habit():
    if len(habits) < HABIT_LIMIT:
        habit_name = habit_entry.get().strip()  # Strip whitespace from input
        if habit_name:
            habits.append({'name': habit_name, 'streak': 0, 'completed': False, 'last_checked': 0})
            habit_entry.delete(0, tk.END)
            save_habits()
            update_habit_list()  # Update the habit list
            # After updating the habit list, scroll to the last habit
            scroll_to_last_habit()
            messagebox.showinfo("Habit Added", f"Habit '{habit_name}' added successfully!")  # Confirmation message
        else:
            messagebox.showwarning("Input Error", "Please enter a habit name.")
    else:
        messagebox.showwarning("Limit Reached", f"You can only add up to {HABIT_LIMIT} habits.")

def reset_habit_streak(index):
    habits[index]['streak'] = 0
    save_habits()
    update_habit_list()

def update_scroll_region():
    # Update the scroll region based on the number of habits
    total_height = len(habits) * 30  # Assuming each habit row is approximately 30 pixels high
    canvas.configure(scrollregion=(0, 0, 0, total_height))

def scroll_to_last_habit():
    # Scroll down to the last habit
    if habits:
        last_habit_position = (len(habits) - 1) * 30  # Assuming each habit row is approximately 30 pixels high
        canvas.yview_moveto(last_habit_position / (len(habits) * 30))  # Move to the last habit

# Function to scroll using mouse wheel (for vertical scrolling)
def on_mousewheel_vertical(event):
    # Get the current vertical position
    current_position = canvas.yview()[0] * canvas.bbox("all")[3]  # Current position in pixels
    if current_position > 0:  # Allow scrolling down only if not at the top
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Function to scroll using shift+mouse wheel (for horizontal scrolling)
def on_mousewheel_horizontal(event):
    # Prevent horizontal scrolling if already at the left
    if event.delta < 0:  # Scrolling right
        canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
    else:  # Scrolling left
        if canvas.xview()[0] > 0:  # Allow scrolling only if not at the left edge
            canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

root = tk.Tk()
root.title("Habit Tracker")
root.geometry("755x440")  # Increased the window size to accommodate a larger frame

# Entry and button area
habit_label = tk.Label(root, text="Enter a habit to track:", font=("Microsoft YaHei UI Light", 14, "italic"), fg="#57a1f8")
habit_label.place(x=200, y=10)

habit_entry = tk.Entry(root, width=30, font=("Microsoft YaHei UI Light", 12))
habit_entry.place(x=200, y=50)

submit_button = tk.Button(root, text="Add Habit", command=add_habit, font=("Microsoft YaHei UI Light", 12), fg="#57a1f8")
submit_button.place(x=250, y=90)

# Create a frame for the fixed headers (non-scrollable)
header_frame = tk.Frame(root)
header_frame.place(x=20, y=130, width=715)

# Create column headers (fixed)
tk.Label(header_frame, text="Checkbox", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(header_frame, text="Habit Name", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
tk.Label(header_frame, text="Actions", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)


# Create a frame for the canvas and scrollbar
canvas_frame = tk.Frame(root)
canvas_frame.place(x=20, y=160, width=715, height=250)

# Create the canvas for habit list
canvas = tk.Canvas(canvas_frame, width=715, height=250)  # Fixed height for the canvas
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add vertical scrollbar
scrollbar_vertical = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

# Add horizontal scrollbar
scrollbar_horizontal = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the canvas to work with the scrollbars
canvas.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Bind mouse wheel event to the canvas for vertical scrolling
canvas.bind_all("<MouseWheel>", on_mousewheel_vertical)

# Bind Shift + MouseWheel event to the canvas for horizontal scrolling
canvas.bind_all("<Shift-MouseWheel>", on_mousewheel_horizontal)

# Create a frame inside the canvas to hold the habit list
habit_list_frame = tk.Frame(canvas, width=715)  # Increased the size of the habit list frame
canvas.create_window((0, 0), window=habit_list_frame, anchor="nw")

habits = load_habits()
update_habit_list()

root.mainloop()
