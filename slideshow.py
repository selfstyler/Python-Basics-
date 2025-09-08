from itertools import cycle
from PIL import Image, ImageTk
import time 
import tkinter as tk

root=tk.Tk()
root.title("Image SLideshow Viewer")
 
 #List of Image Path 
image_paths =[
    
    r"C:\Users\Lenovo\Pictures\Camera Roll\WhatsApp Image 2024-08-17 at 23.10.06_4cf41dad.jpg",
    r"C:\Users\Lenovo\Pictures\Camera Roll\WhatsApp Image 2024-08-20 at 23.08.20_25422975.jpg",
    r"C:\Users\Lenovo\Pictures\Camera Roll\WIN_20250207_15_43_41_Pro.jpg",
]

#Setiing image in to a perfect soze 1080x1080
image_size=(1080,1080)
images=[Image.open(path). resize(image_size) for path in image_paths]
photos_images=[ImageTk.PhotoImage(image) for image in images]
label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photos_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)
        
        
slideshow = cycle(photos_images)


def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()
        
play_button = tk.Button(root, text='Play', command=start_slideshow)
play_button.pack()

root.mainloop()

