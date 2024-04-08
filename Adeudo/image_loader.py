from tkinter import PhotoImage
from PIL import Image, ImageTk

class ImageLoader:
    def __init__(self):
        self.logo1_image = self.load_image("logo1.png", (180, 100))
        self.logo2_image = self.load_image("logo2.png", (180, 100))
        self.icon_image = self.load_image("logo4.ico", (180, 100))

    def load_image(self, path, size):
        image = Image.open(path)
        image = image.resize(size)
        return ImageTk.PhotoImage(image)

    def get_logo1(self):
        return self.logo1_image

    def get_logo2(self):
        return self.logo2_image

    def get_icon(self):
        return self.icon_image
