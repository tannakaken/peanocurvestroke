from pixelization import pixelization
from peano import Peano
import sys

data = pixelization(sys.argv[1])
size = 8100
peano = Peano(size,size)
peano.stroke_array(size, size, data)
peano.save("peano.png")
