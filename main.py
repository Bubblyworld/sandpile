#!/usr/bin/env python3
import math as m
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from PIL import Image, ImageColor
from src.sandpile import Sandpile
from test import ana, top

# Global configuration:
WIDTH = 100
HEIGHT = 100
COLORS = ['red', 'green', 'blue', 'purple']

# Identity element of the critical group.
#e = Sandpile.identity(WIDTH, HEIGHT).grid

# Computing u8.
e = Sandpile(WIDTH, HEIGHT)
e.vadd(e.const(4))
cnt = e.stabilise()

tg = e.topplegrid
w = tg.shape[0]
h = tg.shape[1]
x = np.linspace(0, w-1, w, dtype=float)
y = np.linspace(0, h-1, h, dtype=float)
X, Y = np.meshgrid(x,y)


# Need to get these functions at the point where max(ana) <= 3
u = ana(X, Y, cnt, WIDTH*1.0, 5, 5)
v = top(X, Y, cnt, WIDTH*1.0, 5, 5)

fig, axes = plt.subplots(2, 2, subplot_kw={"projection": "3d"})
axes[0, 0].plot_surface(X, Y, e.grid, cmap="cool")
axes[0, 1].plot_surface(X, Y, tg, cmap="cool")
axes[1, 0].plot_surface(X, Y, u, cmap="cool")
axes[1, 1].plot_surface(X, Y, v, cmap="cool")
plt.show()

# A general quadratic in x, y.
def quad(x, y, a, b, c, d):
    return a*x*y + b*(x+y)*(x+y) + c*(x+y) + d

# Restructured to satisfy scipy.curve_fit requirements.
def _quad(M, *args):
    x, y = M
    return quad(x, y, *args)

# Regress a topplegrid onto a general 2-variable quadratic.
def regress_quad(topplegrid):
    w = topplegrid.shape[0]
    h = topplegrid.shape[1]
    x = np.linspace(0, w-1, w, dtype=int)
    y = np.linspace(0, h-1, h, dtype=int)

    X, Y = np.meshgrid(x,y)
    xdata = np.vstack((X.ravel(), Y.ravel()))
    ydata = topplegrid.ravel()
    popt, _ = curve_fit(_quad, xdata, ydata, (1.0, 1.0, 1.0, 1.0))

# Draw a pretty image of it:
#for i in range(100):
#    img = Image.new('RGB', (WIDTH, HEIGHT))
#    for x in range(WIDTH):
#        for y in range(HEIGHT):
#            img.putpixel((x, y), ImageColor.getrgb(COLORS[e.grid[x, y]]))
#
#    print("Saving " + str(i))
#    img.save('artifacts/img_'+str(i)+'.png')
#
#    e.vadd(e.grid)
#    e.stabilise()
