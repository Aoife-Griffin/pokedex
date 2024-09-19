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

### Function to load pokemon

def load_pokemon():
    # Get name or id that was passed in from starting to end poisition
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    # Get sprite
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    
    # Turn image into bytes and save to object
    image = PIL.Image.open(BytesIO(response.data))
    # Turn object into tkinter
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    # Get information
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())

    # Get type
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())


### Search for Pokemon
label_id_name = tk.Label(window, text="Name or Number")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

button_load = tk.Button(window, text="Find Pokemon", command=load_pokemon)
button_load.config(font=("Arial", 20))
button_load.pack(padx=10, pady=10)




window.mainloop()