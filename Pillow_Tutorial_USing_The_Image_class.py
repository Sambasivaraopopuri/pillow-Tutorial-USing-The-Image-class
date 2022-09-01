from PIL import Image
im = Image.open("keerthi.jpg")
print(im.format, im.size, im.mode)