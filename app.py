import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk


# beginning of interface
# All element created inside these two lines
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#Instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Montserrat")
instructions.grid(columnspan=3, column=0, row=1)


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Montserrat", bg="#20bebe", fg="white", height=2)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


root.mainloop()
#elements wont appear in object below this command