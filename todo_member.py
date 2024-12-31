
# Import necessary modules
import tkinter as tk 
from tkinter import messagebox
# Member 1

# Define the TodoList class
class TodoList:
  def __init__(self, master):
    # Initialize the main window
    self.master = master
    self.master.title("Todo List - Group One")
    
    # Initialize task storage
    self.tasks = []

    # Task Entry
    self.task_entry = tk.Entry(self.master, width=50)
    self.task_entry.grid(row=0, column=0, padx=10, pady=10)

    # Add task button
    self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
    self.add_button.grid(row=0, column=1, padx=5, pady=10)

    # Listbox for tasks
    self.task_listbox = tk.Listbox(self.master, width=50)
    self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Delete task button
    self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
    self.delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
# Member 2

  # Method to add a task
  def add_task(self):
    # Get the task from the entry
    task = self.task_entry.get()
    if task:
      self.tasks.append(task)
      self.task_listbox.insert(tk.END, task)
      self.task_entry.delete(0, tk.END)
    else:
      messagebox.showwarning("Warning", "Please Enter a task")
# Member 3

  # Method to delete a task
  def delete_task(self):
    try:
      # Get the selected task index
      index = self.task_listbox.curselection()[0] 
      # Remove the task from the listbox and task storage
      self.task_listbox.delete(index)
      del self.tasks[index]
    except IndexError:
      # Show a warning if no task is selected
      messagebox.showwarning("Warning", "Please select a task to delete")
# Member 4

# Create the main application window
root = tk.Tk()
# Create an instance of TodoList
todo_app = TodoList(root)

# Start the application loop
root.mainloop()
# Member 5

