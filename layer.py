import math
from color import Color


class Layer:
    """Class that stores the pixel data of an image layer"""

    from _simple_transformations import flip_horizontal_axis
    from _simple_transformations import flip_vertical_axis
    from _simple_transformations import rotate_counter_clockwise

    from _advanced_transformations import color_at
    from _advanced_transformations import interpolate_bilinear
    from _advanced_transformations import interpolate_nearest_neighbor
    from _advanced_transformations import rotate_same_size
    from _advanced_transformations import scale_backward
    from _advanced_transformations import scale_forward
    from _advanced_transformations import translate
    from _advanced_transformations import get_in_place_matrix
    from _advanced_transformations import get_expanded_matrix
    from _advanced_transformations import rotate_expand

    


    def __init__(self, width: int, height: int, offset_x: float, offset_y: float):
        """Store the constructor arguments"""
        self.width, self.height = width, height
        self.offset_x, self.offset_y = offset_x, offset_y
        self.pixels = [0, 0, 0] * self.width * self.height

    def generate_histogram(self):
        layer = Layer(255, 100, 0,0)

        histogram = [0] * 256
        for y in range(self.height):
            for x in range(self.width):
                pixel = self.get_pixel(x,y)
                grayscale = math.floor((pixel[0] + pixel[1] + pixel[2])/3)
                histogram[grayscale]+=1

        max = 0
        for h in histogram:
            if h > max:
                max = h
        
        # Now normalize the histogram
        histogram_max = 100
        for i in range(256):
            h = histogram[i]
            h /= max
            h *= histogram_max
            histogram[i] = h

        # Draw the histogram
        for i in range(256):
            layer.set_pixel(math.floor(i), math.floor(histogram[i]), (255,255,255))

        return layer

    def set_pixel(self, x, y, color) -> None:
        """Set a pixel in the layer buffer"""
        index = self.pixelIndex(x, y)
        self.pixels[y*self.width+x] = color

    def get_pixel(self, x: int, y: int):
        """ Given x and y, return the color of the pixel"""
        index = self.pixelIndex(x, y)
        return self.pixels[index]

    def pixelIndex(self, x:int, y:int) -> int:
        """Given x and y, find the index in our linear array."""
        index = y*self.width + x
        return index

   
    