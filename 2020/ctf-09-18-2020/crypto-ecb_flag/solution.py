import numpy as np
from PIL import Image

WIDTH = 1920
HEIGHT = 1080
CHANNELS = len('RGBA')

# Open image
f = open('flag_encrypted.dat', 'rb')
img = bytearray(f.read())
f.close()

# Display bytes as image
img = np.frombuffer(img, dtype = np.uint8)
img = np.reshape(img, newshape = (HEIGHT, WIDTH, CHANNELS))
img = Image.fromarray(img)
img.show()
