# This program requires pillow
# `python -m pip` to install pillow

from PIL import Image
from container import Container
from layer import Layer
import cProfile
import time
import math
import numpy as np
import os


def main():
    print("Start")

    dir = "./images/"
    files = os.listdir(dir)
    for file in files:
        #Auto tune
        container = get_layers_in_a_row(3, dir + file)
        container.layers[1].auto_tune_brightness()
        container.layers[2].auto_tune_brightness()
        container.layers[2].auto_tune_contrast()
        # layer1.auto_tune_brightness()
        # layer1.auto_tune_contrast()
        container.add_layer(container.layers[0].generate_histogram())
        container.add_layer(container.layers[1].generate_histogram(), container.layers[1].width, 0)
        container.add_layer(container.layers[2].generate_histogram(), container.layers[2].width*2, 0)
        container.pack()

        # Finally, save the image
        print("Done with " + file)
        container.save("done_" + file + ".png")
        # break

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
#cProfile.run("main()", "c:/tmp/tmp.prof")
end = time.time()
print(str(end - start) + " " + " seconds")
