from PIL import Image
import numpy as np

def pixelization(filename):
    im = Image.open(filename)
    monochrome_im = im.convert('L')
    small_im = monochrome_im.resize((49,49))

    arr = np.array(small_im)
    arr = 7 - (arr / (256/8))
    arr = arr.astype(np.uint8)

    return arr

if __name__ == '__main__':
    pixelization('../Lenna.png')
