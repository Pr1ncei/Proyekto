"""
HOMEWORK MANAGER using TKINTER

Pre-Development Grasp:
The project aims to create a Tkinter-based GUI application to help users manage their homework, projects, or tasks in general. It is basically like a TO-DO List app but with notification and priority system. The application will allow users to add and remove tasks, set deadlines, and add descriptions. A tab view will show the remaining days until the deadline, and detailed descriptions will be displayed upon clicking a task. The GUI will be responsive, ensuring it looks good on different screen sizes, and will potentially support custom resolution.

Other Ideas:
- On the startup of the app, the default view will be the tab view or the overview of the tasks.
- Then the task manager (adding, removing) the homeworks will be set on the side view
- Add Notification System abd Priority System by using colors

Initial Steps:
- Basic GUI Setup:
    - Tkinter
    - Main Window
    - Add Title

- Make the GUI Responsive
    - Grid Layout
    - Window Resizing

- Implement Basic Features:
    - Add & Remove Homework/Projects:
        - Create buttons to add and remove tasks.
    - Implement an input field for the task description and a date picker for the deadline.

- Default Tab View on Startup
    - When the app starts, it will open directly to the tab view, showing the list of app tasks with their remaining days until the deadline
        - use the Notebook widget from Tkinter's ttk module to create tabs

- Side View Tab [ONGOING]
    - By using PanedWindow, the utilities will be positioned on the side bar on the main window, like on Canvas

- Notification and Priority System
    - Notification System:
        - Set up notifications that alert users when a deadline is approaching.
        - Implementation: Use a timer or scheduler to check deadlines periodically and display a pop-up or a message on the screen when a task is due soon.

    - Priority System Using Colors:
        - Tasks will be color-coded based on their priority, making it easy to distinguish high-priority tasks at a glance.
        - Implementation: Assign colors to tasks based on their priority level (e.g., red for high priority, yellow for medium, green for low). You can use the tag_configure method of the Treeview or Listbox widget to apply colors.

In Progress:
- Responsive GUI
- Adding Side View Tab and Switching Multiple Pages

References:
- Notion App
- Canvas

"""

# Progress: Ongoing

# Setting the GUI up first (08-24-2024)
from tkinter import *
import tkinter as tk
from customtkinter import * # For Designing purposes in the future

root = tk.Tk()
root.geometry('800x600')
root.title("HOMEWORK MANAGER")
root.configure(background="white") # Main Background

# SETTINGS
def toggle_menu():
    if options_frame.winfo_ismapped():
        options_frame.pack_forget()
        toggle_btn.config(text='☰')
    else:
        options_frame.pack(side=tk.LEFT, fill='y')
        toggle_btn.config(text='X')

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root)

    window_height = root.winfo_height()

    toggle_menu_fm.place(x=0,y=50, height=window_height, width=200)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)

# Page Content - This is where you put the main program of the homework program
def task_page():
    task_frame = tk.Frame(main_frame)

    lb = tk.Label(
        task_frame,
        text='Task Page\n\nPage: 1',
        font=('Bold, 30')
    )
    lb.pack()
    task_frame.pack(pady=20)

def option_page():
    option_frame = tk.Frame(main_frame)

    lb = tk.Label(
        option_frame,
        text='Option Page\n\nPage: 2',
        font=('Bold, 30')
    )
    lb.pack()

    option_frame.pack(pady=20)

# Indicator
def hide_indicator():
    task_indicator.config(bg='#08002f')
    option_indicator.config(bg='#08002f')

def indicate(button, page):
    hide_indicator()
    button.config(bg='white')
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

# Side Bar
options_frame = tk.Frame(root, bg="#08002f")

# Buttons

toggle_btn = tk.Button(options_frame,
    text='☰',
    bg = '#08002f',
    fg = 'white',
    font = ("Bold, 20"),
    bd = 0,
    activebackground='#08002f',
    activeforeground='white',
    command=toggle_menu
)

toggle_btn.place(x=5, y=0)

    # TASK
task_btn = tk.Button(
        options_frame,
        text='Tasks',
        font=("Bold, 15"),
        fg='white',
        bd=0,
        background='#08002f',
        command=lambda: indicate(task_indicator, task_page)
    )
task_btn.place(x=17, y=50)

    # OPTIONS (Placeholder)
option_btn = tk.Button(
        options_frame,
        text="Options",
        font=("Bold, 15"),
        fg="white",
        bd=0,
        background="#08002f",
        command=lambda: indicate(option_indicator, option_page)
    )

option_btn.place(x=11, y=100)

# INDICATORS
# Shows an indicator if you're on this page
task_indicator = tk.Label(options_frame, text='', bg="#08002f")
task_indicator.place(x=3, y=50, width=5, height=40)

# Shows an indicator if you're on this page
option_indicator = tk.Label(options_frame, text='', bg="#08002f")
option_indicator.place(x=3, y=100, width=5, height=40)

options_frame.pack(side=tk.LEFT, fill="y")
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)

# Main Frame
main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT, fill="both", expand=TRUE)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=400)


# To make it responsive, add on the 'pack()', "fill="x"/y or fill="both", expand=True . See the sample above

# Output
root.mainloop()

# Notes:
# PLEASE ORGANIZE IT ONCE YOU FINISHED THE GUI BEFORE MAKING THE ACTUAL PROGRAM, THANK YOU - Prince (08/25/2024)

# Major Bug:
# If you hide the side bar, you can't get the side bar back.