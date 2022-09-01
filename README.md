# pillow-Tutorial-USing-The-Image-class

Tutorial
Using the Image class
#Step-1 
Install PILLOW :- pip install pillow

#Step-2
Connect pillow in our python file
from PIL import Image

#step-3
our python file level put one or more images
image = Image.open("hopper.ppm")

#Print Image Size,format, mode
print(image.format, image.size, image.mode)
#Run our file through this command :- python Pillow_Tutorial_USing_The_Image_class.py
output: JPEG (289, 175) RGB

#Show image
image.show()
#Run our file through this command :- python Pillow_Tutorial_USing_The_Image_class.py

