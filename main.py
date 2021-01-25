# Imports PIL module  
from PIL import Image 
  
# open method used to open different extension image file 
im = Image.open(r"image.jpg")  
  
# This method will show image in any image viewer  
im.show()