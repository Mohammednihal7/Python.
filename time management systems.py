import tkinter as tk
from tkinter import*
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

def schedule_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x.priority, reverse=True)
    schedule = []
    current_time = datetime.now()

    for task in sorted_tasks:
        end_time = current_time + timedelta(minutes=task.duration)
        schedule.append((task.name, current_time.strftime("%H:%M"), end_time.strftime("%H:%M")))
        current_time = end_time

    return schedule

def display_schedule():
    schedule = schedule_tasks(tasks)
    schedule_window = tk.Toplevel(root)
    schedule_window.title("Scheduled Tasks")
    schedule_window.geometry("400x300")

    for index, (task, start_time, end_time) in enumerate(schedule, start=1):
        schedule_label = tk.Label(schedule_window, text=f"{index}. {task} - Start: {start_time}, End: {end_time}")
        schedule_label.pack(pady=5)

def add_task():
    name = name_entry.get()
    duration = duration_entry.get()
    priority = priority_entry.get()

    if name and duration and priority:
        try:
            duration = int(duration)
            priority = int(priority)
            tasks.append(Task(name, duration, priority))
            update_task_list()
            clear_entry_fields()
        except ValueError:
            messagebox.showerror("Error", "Duration and Priority must be integers.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        del tasks[selected_index]
        update_task_list()
    except IndexError:
        pass

def clear_entry_fields():
    name_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, f"{task.name} ({task.duration} mins, Priority: {task.priority})")

tasks = []

root = tk.Tk()
root.title("Time Management System")
root.geometry("600x400")

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Task entry fields
name_label = tk.Label(main_frame, text="Task Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(main_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

duration_label = tk.Label(main_frame, text="Duration (mins):")
duration_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
duration_entry = tk.Entry(main_frame)
duration_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

priority_label = tk.Label(main_frame, text="Priority (1-10):")
priority_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
priority_entry = tk.Entry(main_frame)
priority_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

add_button = tk.Button(main_frame, text="Add Task", command=add_task)
add_button.grid(row=3, column=1, padx=5, pady=5, sticky="we")

delete_button = tk.Button(main_frame, text="Delete Selected Task", command=delete_task)
delete_button.grid(row=4, column=1, padx=5, pady=5, sticky="we")

# Task list
task_list = tk.Listbox(main_frame, height=10)
task_list.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Schedule button
schedule_button = tk.Button(main_frame, text="Create Schedule", command=display_schedule)
schedule_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        

        
        

update_task_list()

root.mainloop()

