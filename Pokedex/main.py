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

### Add data for Pokemon
pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 24))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 24))
pokemon_types.pack(padx=10, pady=10)





window.mainloop()