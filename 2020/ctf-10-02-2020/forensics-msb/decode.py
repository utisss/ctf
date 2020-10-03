from PIL import Image

img = Image.open('meme.png')
pixels = img.load()
width, height = img.size
val = 0
msg = ''
# iterate over the pixels of the image, columns first
for i in range(width):
    for j in range(height):
        n = (i * width) + j
        # if we've read 8 bytes, record the character and reset
        if n % 8 == 0 and n > 0:
            msg += chr(val)
            val = 0
        # get a bit of the message from the MSB
        pix = pixels[i,j]
        mask = 1 << 7
        if pix[0] & mask != 0:
            val += 1
        if n % 8 < 7:
            val <<= 1
print('recovered message: '+msg)

