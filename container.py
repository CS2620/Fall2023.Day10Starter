from layer import Layer
from PIL import Image

class Container:
  """A list of layer objects
  
  Args:
    width (int): The width of the container
    height (int): The height of the container
  """
  def __init__(self, width:int, height:int):
    self.width, self.height = width, height
    self.image = Image.new("RGB", (width, height))
    self.buffer = self.image.load()
    self.layers = []

  def add_layer(self, layer:Layer, offset_x = 0, offset_y = 0):
    """Add a layer to the container
    
    Args:
      layer (Layer): The layer to add to the container
    """
    layer.parent = self
    layer.offset_x = offset_x
    layer.offset_y = offset_y
    
    self.layers.append(layer)

  def resize(self, width, height):
    self.width, self.height = width, height
    self.image = Image.new("RGB", (width, height))
    self.buffer = self.image.load()
    

  def save(self, filename):
    """
    Rasterize and save the layers
    
    Step 1: Rasterize all layers to this container's buffer
    Step 2: Save that buffer to the filesystem

    Args:
      filename (string): The filename to save to
    """
    for layer in self.layers:
      ox = layer.offset_x
      oy = layer.offset_y
      # if oy < 0:
      #   oy = self.height - oy
      for y in range(min(layer.height, self.height)):
        for x in range(min(layer.width, self.width)):
          color = layer.get_pixel(x,y)
          self.buffer[x+ox,y+oy] = color
    self.image.save(filename, "png")

  

