#To clear the remaining black squares after the first bath

try:
    import Image
except ImportError:
    from PIL import Image

import sys
import math




def clear(im):

    im = im.convert("1")
    data = im.load()
    width, height = im.size

    flag = 0
    x = 1
    y = 1

    def noise(x,y):
    #To determine whether the pixel is noise or not depending on the colors of the four pixels from each of which are two units aparts.
    #The pixel is reckoned as noise where the four pixels are all while dots.
    #    o
    #
    # o  i  o
    #
    #    o
    # (noise)

        check = True
        i = x
        j = y
        if data[i,j-2] <> 255:
            check = False

        if data[i,j+2] <> 255:
            check = False

        if data[i-2,j] <> 255:
            check = False

        if data[i+2,j] <> 255:
            check = False
        return check


    for y in range(height):
        if (y % 15 == 2) or (y % 15 == 3):
            #print y % 15
            for x in range(width):
                #If every pixel is white, flag remains the same
                if x % 15 == 13 or 14:
                    if data[x, y] > 200:
                        continue
                    #If the pixel is black, raise the flag
                    if data[x, y] < 200:
                        #If the pixel is noise, wipe it out
                        #print "(" + str(x) + "," + str(y) + ")"
                        if noise(x,y) == 1:
                            data[x,y] = 255
                        else:
                            continue
                        #flag = 1
                        #print "(" + str(x) + "," + str(y) + ")"
                else:
                    continue
        else:
            continue

    return  im



