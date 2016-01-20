try:
    import Image
except ImportError:
    from PIL import Image

from bath import *
from clearNoise import *

#from pytesser import image_to_string

import os

def image_to_string(img, cleanup=True, plus =''):
    os.popen('tesseract bath_again.png result')
    text = file('result.txt').read().strip()
    if cleanup:
        os.remove('result.txt')
    return text

def code():
    im = Image.open(r'C:\Users\heluoyichong\PycharmProjects\SecurityCode\screenshot.png')
    left = 640
    top = 160
    right = 760
    bottom = 220
    im_crop = im.crop((left, top, right, bottom)) # defines crop points
    im_crop.save("crop.png")
    clear(bath(im_crop)).save("bath.png")
    return image_to_string('bath_again.png')

print(code())