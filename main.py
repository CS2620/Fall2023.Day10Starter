# This program requires pillow
# `python -m pip` to install pillow

from PIL import Image
from container import Container
from layer import Layer
import time
import numpy as np
import os


def main():
    print("Start")

    dir = "./images/"
    files = os.listdir(dir)
    for file in files:
        container = get_layers_in_a_row(1, dir + file)
        container.add_layer(container.layers[0].generate_histogram())
        container.pack()

        # Finally, save the image
        print("Done with " + file)
        container.save("done_" + file + ".png")
        break

def get_layers_in_a_row(count, filename):
    if count <= 0:
        return print("You need to generate more than 0 layers")
    if not filename:
        return print("You forgot to all a filename")
    
    layers = []

    image = Image.open(filename)
    """ Load the image and get its height and width"""
    width = image.size[0]
    height = image.size[1]

    """ Building a container for the image"""
    container: Container = Container(width, height)
    for i in range(count):
        layer: Layer = Layer(width, height, 0, 0)
        layer.pixels = list(image.getdata())
        container.add_layer(layer, layer.width * i)
    
    return container

    


start = time.time()
main()
end = time.time()
print(str(end - start) + " " + " seconds")
