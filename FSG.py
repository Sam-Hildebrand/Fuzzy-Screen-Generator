#!/usr/bin/python3

# A simple program that generates an random image, intended to
# look vaguely like the "fuzzy" screen on old satelite tv in rainy
# weather.


import random
from PIL import Image
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def PickColors(RedL, GreenL, BlueL):
	Red   = random.randint(0, RedL)
	Green = random.randint(0, GreenL)
	Blue  = random.randint(0, BlueL)
	return(Red, Green, Blue)

def GenImage(Width, Height, RedL, GreenL, BlueL):
	img = Image.new('RGB',(Width,Height))
	for i in range(Width):
		for j in range(Height):
			img.putpixel((i,j),PickColors(RedL, GreenL, BlueL))
	return(img)

class Handler:
    def quit(self, *args):
        Gtk.main_quit()

    def save(self, *args):
        print(name.get_text())
        print(width.get_text())
        print(height.get_text())
        print(red.get_text())
        print(green.get_text())
        print(blue.get_text())
        img = GenImage(int(width.get_text()), int(height.get_text()), int(red.get_text()), int(green.get_text()), int(blue.get_text()))
        filename = str(name.get_text()) + ".png"
        img.save(filename)
        imagewin = Gtk.Window(title="image")
        imagewin.add(Gtk.Image.new_from_file(filename))
        imagewin.show_all()

if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("gui.glade")
    builder.connect_signals(Handler)
    window = builder.get_object("window")
    image = builder.get_object("image")
    name = builder.get_object("name")
    width = builder.get_object("width")
    height = builder.get_object("height")
    red = builder.get_object("red")
    green = builder.get_object("green")
    blue = builder.get_object("blue")

    window.show_all()
    window.connect("destroy", Gtk.main_quit)

    Gtk.main()
