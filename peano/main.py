#!/usr/bin/env python3
from PIL import Image,ImageDraw
import sys

class Peano:
    """
    ペアノ曲線の構成法による一筆書きを行うための画像データと
    ペンの現在位置を保持するクラス
    """
    def __init__(self, width, height):
        """
        画像データを幅と高さで初期化して、
        ペンの位置を画面左上の原点に置く。

        Parameters
        ----------
        width : int
            画像の幅
        height : int
            画像の高さ
        """
        self.image = Image.new('RGB', (width, height), (255,255,255))
        self.drawing = ImageDraw.Draw(self.image)
        self.x = 0
        self.y = 0

    def show(self):
        """
        現在の画像の状態をGUIで表示する。
        """
        self.image.show()

    def save(self, filename):
        """
        現在の画像データをファイルに保存する。

        Parameters
        ----------
        filename : str
            画像を保存するファイル名
        """
        self.image.save(filename)

    def goto(self, x,y):
        """
        ペンを移動させながら線を引く。

        Parameters
        ----------
        x : int
            移動先のx座標
        y : int
            移動先のy座標
        """
        self.drawing.line((self.x, self.y, x, y), fill=(0,0,0), width=1)
        self.x = x
        self.y = y
    
    def unit(self, x, y, width, height):
        """
        ペアノ曲線の一番単純な１つ分の曲線（単位ペアノと呼ぶことにする）を描く。

        Parameters
        ----------
        x : int
            単位ペアノを描く長方形の左上のx座標
        y : int
            単位ペアノを描く長方形の左上のy座標
        width : int
            単位ペアノを描く長方形の幅
        height : int
            単位ペアノを描く長方形の高さ
        """
        self.goto(x + width/6, y + height/6)
        self.goto(x + width*5/6, y + height/6)
        self.goto(x + width*5/6, y + height/2)
        self.goto(x + width/6, y + height/2)
        self.goto(x + width/6, y + height*5/6)
        self.goto(x + width*5/6, y + height*5/6)

    def stroke(self, x, y, width, height, depth):
        """
        ピクセルを3x3分割して
        再帰的にペアノ曲線を描いていく。

        Parameters
        ----------
        x : int
            ペアノ曲線を描く長方形の左上のx座標
        y : int
            ペアノ曲線を描く長方形の左上のy座標
        width : int
            ペアノ曲線を描く長方形の幅
        height : int
            ペアノ曲線を描く長方形の高さ
        depth : int
            0〜7で表現された色の濃さ。（正確には対応しないが）再帰の深さ
        """
        if depth <= 0:
            self.unit(x, y, width, height)
        else:
            new_width = width/3
            new_height = height/3
            if depth % 3 == 0:
                odd_depth = depth - 2
                even_depth = depth - 5
            elif depth % 3 == 1:
                odd_depth = depth - 3
                even_depth = depth - 3
            else:
                odd_depth = depth - 4
                even_depth = depth - 1
            self.stroke(x, y, new_width, new_height, odd_depth)
            self.stroke(x+new_width, y+new_height, new_width, -new_height, even_depth)
            self.stroke(x+2*new_width, y, new_width, new_height, odd_depth)
            self.stroke(x+width, y+new_height, -new_width, new_height, even_depth)
            self.stroke(x+2*new_width, y+2*new_height, -new_width, -new_height, odd_depth)
            self.stroke(x+new_width, y+new_height, -new_width, new_height, even_depth)
            self.stroke(x, y+2*new_height, new_width, new_height, odd_depth)
            self.stroke(x+new_width, y+height, new_width, -new_height, even_depth)
            self.stroke(x+2*new_width, y+2*new_height, new_width, new_height, odd_depth)

    def stroke_array(self, width, height, data):
        """
        二重配列dataの内容に沿って、
        ペアノ曲線による一筆描き（ペアノ一筆書きと呼ぶことにする）で、
        画像に線を描いていく。

        Parameters
        ----------
        width : int
            ペアノ一筆描きする領域の幅
        height : int
            ペアノ一筆描きする領域の高さ
        data : nump: numpy.ndarray
            画像のピクセルの色の濃さを８段階(0〜7)で表したnumpy二重配列
        """
        rows, columns = data.shape
        x = 0
        y = 0
        wunit = width/columns
        hunit = height/rows
        for row in data:
            if (wunit < 0):
                row = row[::-1]
            for column in row:
                self.stroke(x, y, wunit, hunit, column)
                x += wunit
                y += hunit
                hunit = -hunit
            wunit = -wunit
            hunit = -hunit

if __name__ == '__main__':
    size = 270
    peano = Peano(size,size)
    depth = int(sys.argv[1])
    peano.stroke(0,0,size,size,depth)
    peano.show()
    peano.save("peano" + str(depth) + ".png")
