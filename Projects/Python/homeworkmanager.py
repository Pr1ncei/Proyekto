"""
HOMEWORK MANAGER using TKINTER

The program uses a GUI from TKINTER only
- Add Title 
- And a rough grasp of the project (Pre-development)
- Make the GUI Responsive 

Features:
1. Add & Remove Homework/Projects
    a. Put a deadline by typing or picking it on a calendar (GUI)
    b. Add Description of the Homework
2. Tab view of the homework
    a. shows the remaining days of the homework, but once click it, it will show the description of the homework
    b. if there are no homework, show something like "Take a break"

BONUS:
- Custom Resolution

References:
- Notion App
"""
# Progress: Ongoing

# Setting the GUI up first (08-24-2024)
from tkinter import *
import tkinter as tk 

root = tk.Tk()
root.title("HOMEWORK MANAGER")
root.minsize(800,600)

root.mainloop() # Output