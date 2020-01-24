#!/usr/bin/python3

import random
from tqdm import tqdm
from PIL import Image
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def PickColors(RedL, GreenL, BlueL):
	Red   = random.randint(0, RedL)
	Green = random.randint(0, GreenL)
	Blue  = random.randint(0, BlueL)
	return(Red, Green, Blue)

def GetInput():
	print("Enter the name of the image to generate (the script adds '.png'): ")
	Name = input()
	print("Enter the width: ")
	Width = int(input())
	print("Enter the height: ")
	Height = int(input())
	print("Enter the level for each color (0-255): ")
	print("Red:")
	RedL =  int(input())
	print("Green:")
	GreenL =  int(input())
	print("Blue:")
	BlueL = int(input())
	return(Name, Width, Height, RedL, GreenL, BlueL)

def GenImage(Width, Height, RedL, GreenL, BlueL):
	img = Image.new('RGB',(Width,Height))
	for i in tqdm(range(Width)):
		for j in range(Height):
			img.putpixel((i,j),PickColors(RedL, GreenL, BlueL))
	return(img)

class Handler:
    def quit(self, *args):
        Gtk.main_quit()

if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("gui.glade")
    builder.connect_signals(Handler)
    window = builder.get_object("window")
    [Name, Width, Height, RedL, GreenL, BlueL] = GetInput()
    img = GenImage(Width, Height, RedL, GreenL, BlueL)
    img.save(Name + ".png")
    print("Image generated:")
    print(img)
    #pixbuf = Gdk.pixbuf_new_from_file(Name + ".png")
    #pixbuf = pixbuf.scale_simple(200, 200, Gdk.INTERP_BILINEAR)
    #window.add(Gtk.Image.new_from_file(Name + ".png"))
    #window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
