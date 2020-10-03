from PIL import Image

flag = 'utflag{0n3_1mp0st0r_r3ma1n5}\n'
# gets a bit from the flag
def flag_bit(n):
    # 8 bits per char, encode high->low bits
    char_pos = (n // 8) % len(flag)
    bit_pos = 7 - (n % 8)
    val = ord(flag[char_pos])
    mask = 1 << bit_pos
    return val & mask != 0

img = Image.open('meme-original.png')
pixels = img.load()
width, height = img.size
assert width*height >= len(flag), 'message is too large for image'
# iterate over the pixels of the image, columns first
for i in range(width):
    for j in range(height):
        n = (i * width) + j
        pix = pixels[i,j]
        r, g, b = pix[0], pix[1], pix[2]
        # set the most significant bit of R, G, and B to be the current bit in the image
        if flag_bit(n):
            mask = 1 << 7
            pixels[i,j] = (r | mask, g | mask, b | mask)
        else:
            mask = (1 << 7) - 1
            pixels[i,j] = (r & mask, g & mask, b & mask)

img.save('meme.png')

