import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
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

### Search for Pokemon
label_id_name = tk.Label(window, text="Name or Number")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

button_load = tk.Label(window, text="Find Pokemon")
button_load.config(font=("Arial", 20))
button_load.pack(padx=10, pady=10)






window.mainloop()