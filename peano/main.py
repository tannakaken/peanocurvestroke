from PIL import Image,ImageDraw
import sys

class Peano:
    def __init__(self, width, height):
        self.image = Image.new('RGB', (width, height), (255,255,255))
        self.drawing = ImageDraw.Draw(self.image)
        self.x = 0
        self.y = 0

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename)

    def goto(self, x,y):
        self.drawing.line((self.x, self.y, x, y), fill=(0,0,0), width=1)
        self.x = x
        self.y = y
    
    def unit(self, x, y, width, height):
        self.goto(x + width/6, y + height/6)
        self.goto(x + width*5/6, y + height/6)
        self.goto(x + width*5/6, y + height/2)
        self.goto(x + width/6, y + height/2)
        self.goto(x + width/6, y + height*5/6)
        self.goto(x + width*5/6, y + height*5/6)

    def stroke(self, x, y, width, height, depth):
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
