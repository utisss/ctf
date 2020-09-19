from PIL import Image
import numpy as np
import ctypes as C

# Load my super secure crypto library
# The device this runs on must support AES-NI and the RAND instruction
lib = C.CDLL('./libencrypt.so')

### BEGIN FUNCTION DEFINITIONS

rand_key_128 = lib.rand_key_128
rand_key_128.argtypes = [C.POINTER(C.c_ubyte)]
rand_key_128.restype = C.c_ubyte

byte_buffer = lib.byte_buffer
byte_buffer.argtypes = [C.c_size_t]
byte_buffer.restype = C.POINTER(C.c_ubyte)

ecb_encrypt_128 = lib.ecb_encrypt_128
ecb_encrypt_128.argtypes = [C.POINTER(C.c_ubyte), C.POINTER(C.c_ubyte), C.POINTER(C.c_ubyte), C.c_size_t]
ecb_encrypt_128.restype = None

### END OF FUNCTION DEFINITIONS

# work with large images
Image.warnings.simplefilter('ignore', Image.DecompressionBombWarning)
img = Image.open('flag.png')

# Prepare image
img = np.asarray(img)
img = img.astype(np.ubyte)
# Contiguous 3D array with dimensions WIDTH x HEIGHT x CHANNELS
img_p = img.ctypes.data_as(C.POINTER(C.c_ubyte))
ln = img.shape[0] * img.shape[1] * img.shape[2]
out_p = byte_buffer(ln)

# Generate key
key = byte_buffer(16)
# Retry generating key until successful
rand_fail = True
while rand_fail:
	if rand_key_128(key) != 0:
		rand_fail = False

# Encrypt image
ecb_encrypt_128(img_p, out_p, key, ln)

# Write image
out = np.ctypeslib.as_array(out_p ,shape=(img.shape[0], img.shape[1], img.shape[2]));
out = bytearray(out)
f = open('flag_encrypted.dat', 'wb')
f.write(out)
f.close()
