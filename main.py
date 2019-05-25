#!/usr/bin/env python3

from pixelization import pixelization
from peano import Peano
import sys
import os.path

for filename in sys.argv[1:]:
    data = pixelization(filename)
    size = 8100
    peano = Peano(size,size)
    peano.stroke_array(size, size, data)
    withoutext, _ = os.path.splitext(filename)
    output_filename = withoutext + "_peanocurved.png"
    peano.save(output_filename)
