from pixelization import pixelization
from peano import Peano

data = pixelization('./Lenna.png')
size = 8100
peano = Peano(size,size)
peano.stroke_array(size, size, data)
peano.save("peano.png")
