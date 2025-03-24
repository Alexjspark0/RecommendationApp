import tkinter as tk
import ttkbootstrap as ttk 
from ttkbootstrap import Label

def show_box(event):
    # Position the box where the mouse is hovering
    box.place(x=event.x_root, y=event.y_root)

def hide_box(event):
    # Hide the box when mouse leaves the text
    box.place_forget()

# Set up the main window
root = tk.Tk()
root.geometry("400x400")

# Create a label with text
label = tk.Label(root, text="Hover over me!", font=("Arial", 14))
label.pack(pady=50)

# Create a box that will appear on hover
box = tk.Label(root, text="I'm a box!", bg="yellow", width=10, height=2)

# Bind the hover events to the label
label.bind("<Enter>", show_box)  # When mouse enters the label
label.bind("<Leave>", hide_box)  # When mouse leaves the label

root.mainloop()

