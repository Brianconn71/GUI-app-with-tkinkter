import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk


# beginning of interface
# All element created inside these two lines
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

root.mainloop()
#elements wont appear in object below this command