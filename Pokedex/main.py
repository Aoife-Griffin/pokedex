import pypokedex
from PIL import image, imageTK
import tkinter as tkinter
import urllib3
### Get image from link and handle bytes
from io import BytesIO

### Build baseline
window = tk.Tk()
window.geometry("500x500")
window.title("Pokedex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Personal Pokedex")
title_label.config(font=("Arial", 24))
title_label.pack(padx=10, pady=10)


window.mainloop()