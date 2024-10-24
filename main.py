import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import io

def opener():
    global down, canvas
    photo = tk.filedialog.askopenfilename()
    img_resize = Image.open(photo)
    i, j = img_resize.size
    print(i, j)
    canvas = tk.Canvas(window, width=i, height=j)
    canvas.grid(column=0, row=0)
    if photo:
        img_tk = ImageTk.PhotoImage(img_resize)

        canvas.create_image(i//2, j//2, image=img_tk, anchor=tk.CENTER)
        canvas.create_text(150, 60, text="Abhilaksh", font=("Purisa", 50))
        canvas.image = img_tk

        down.grid(column=1, row=2)

def downloader():
    xx = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    canvas.postscript(file='temp.ps', colormode='color')
    img = Image.open('temp.ps')
    img.save(xx, 'png')

window = tk.Tk()
window.title("Water marker adder")
window.geometry("1000x1000")
open = tk.Button(window, text="open photo", highlightthickness=0, command=opener)
down = tk.Button(window, text="Download image", highlightthickness=0, command=downloader)
open.grid(column=0, row=0)
# canvas.create_text(0,0,text="hii", fill="white", font=("Helvetica", 24))
window.mainloop()