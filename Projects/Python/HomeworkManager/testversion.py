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

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root)

    # TASK
    task_btn = tk.Button(
        toggle_menu_fm,
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
        toggle_menu_fm,
        text="Options",
        font=("Bold, 15"),
        fg="white",
        bd=0,
        background="#08002f",
        command=lambda: indicate(option_indicator, option_page)
    )

    option_btn.place(x=11, y=100)

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

toggle_btn.place(x=55, y=0)

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