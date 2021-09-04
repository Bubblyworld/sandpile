#!/usr/bin/env python3
import numpy as np
from PIL import Image, ImageColor
from src.sandpile import Sandpile

# Global configuration:
WIDTH = 32
HEIGHT = 32
COLORS = ['red', 'green', 'blue', 'purple']

# Identity element of the critical group.
e = Sandpile.identity(WIDTH, HEIGHT).rgrid()

# Draw a pretty image of it:
img = Image.new('RGB', (WIDTH, HEIGHT))
for x in range(WIDTH):
    for y in range(HEIGHT):
        img.putpixel((x, y), ImageColor.getrgb(COLORS[e[x, y]]))
img.show()
