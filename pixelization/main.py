#!/usr/bin/env python3
from PIL import Image
import numpy as np

def pixelization(filename):
    """画像ファイルを開いて
    画像をモノクロ化し、
    縮小し、
    色の濃さを8段階に量子化して返す。

    Parameters
    ----------
    filename : str
        画像ファイル名

    Returns
    -------
    arr : numpy.ndarray
        モノクロ化され縮小された画像のピクセルの色の濃さを８段階(0〜7)で表現したnumpy二重配列
    """
    im = Image.open(filename)
    monochrome_im = im.convert('L') # モノクロ化
    small_im = monochrome_im.resize((49,49)) # 縮小

    arr = np.array(small_im)
    arr = 7 - (arr / (256/8)) # ピクセルの濃さを8段階に量子化
    arr = arr.astype(np.uint8)

    return arr

if __name__ == '__main__':
    import os.path
    arr = pixelization(os.path.dirname(__file__) + '/../Giuseppe_Peano.jpg')
    print(arr)
