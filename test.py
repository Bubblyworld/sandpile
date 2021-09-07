#!/usr/bin/env python3
import math as m
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from PIL import Image, ImageColor
from src.sandpile import Sandpile

def plot(x, y, u):
    fig, axes = plt.subplots(1, 1, subplot_kw={"projection": "3d"})
    axes.plot_surface(x, y, u, cmap="cool")
    plt.show()

def vplot(x, y, ul):
    fix, axes = plt.subplots(len(ul), len(ul[0]), subplot_kw={"projection": "3d"})
    for n in range(len(ul)):
        for m in range(len(ul[0])):
            if (len(ul) == 1):
                axes[m].plot_surface(x, y, ul[n][m])
            else:
                axes[n, m].plot_surface(x, y, ul[n][m], cmap="cool")
    plt.show()

# Assumes boundary is 0.
def dxx(u, dl):
    u = np.pad(u, ((1, 1), (1, 1))) 
    ul = np.roll(u, -1, axis=1)
    ur = np.roll(u, 1, axis=1)
    return (ul + ur - 2*u)[1:-1, 1:-1] / dl / dl

# Assumes boundary is 0.
def dyy(u, dl):
    u = np.pad(u, ((1, 1), (1, 1))) 
    uu = np.roll(u, -1, axis=0)
    ud = np.roll(u, 1, axis=0)
    return (uu + ud - 2*u)[1:-1, 1:-1] / dl / dl

# Assumes boundary is 0.
def solve(u, dl, dt):
    return u + dt/4 * (dxx(u, dl) + dyy(u, dl))

# Actual analytic solution for u_0 = 4 with truncated fourier series.
# l is the length of the square domain's side.
# N, M are the cutoff values for the fourier coefficients A_nm.
def ana(x, y, t, l, N, M):
    res = np.zeros(x.shape, dtype=float)
    for n in range(1, N+1):
        for m in range(1, M+1):
            res += _ana(x, y, t, l, n, m)
    return res

def _ana(x, y, t, l, n, m):
    const = 64.0 / np.pi**2 / n / m * np.sin(np.pi*n/2)**2 * np.sin(np.pi*m/2)**2
    tval = np.exp(-(n*n + m*m) * np.pi**2 / l**2 / 4 * t)
    return const * tval * np.sin(n * np.pi * x / l) * np.sin(m * np.pi * y / l)

# Analytic solution for the toppling function.
def top(x, y, t, l, N, M):
    res = np.zeros(x.shape, dtype=float)
    for n in range(1, N+1):
        for m in range(1, M+1):
            res += _top(x, y, t, l, n, m) - _top(x, y, 0, l, n, m)
    return res

def _top(x, y, t, l, n, m):
    const = 64.0 / np.pi**2 / n / m * np.sin(np.pi*n/2)**2 * np.sin(np.pi*m/2)**2
    tconst = -1.0 * l**2 / (n*n + m*m) / np.pi**2
    tval = np.exp(-(n*n + m*m) * np.pi**2 / l**2 / 4 * t)
    return const * tconst * tval * np.sin(n * np.pi * x / l) * np.sin(m * np.pi * y / l)

# Generating solutions of the dissipation equation on the unit square:
#   4u_t = u_xx + u_yy
# ...subject to various boundary conditions, like u=0 or the more complex
#    ODE constraints I managed to scrounge from the discrete model.
N = 100
I = 4
DL = 1.0
DT = 1.0 # stability issues, should be order of mag smaller than DL

#t = np.zeros((N+1, N+1), dtype=float)
#u = I * np.ones((N+1, N+1), dtype=float)
#x, y = np.meshgrid(
#    np.linspace(0, N*DL, N+1, dtype=float),
#    np.linspace(0, N*DL, N+1, dtype=float),
#)
#
#time = 0
#while np.max(u) > 3.0:
#    time += DT
#    t += DT * u / 4
#    u = solve(u, DL, DT)
#
#v = ana(x, y, time, N*DL, 2, 2)
#vt = top(x, y, t, N*DL, 10, 10)
#vplot(x, y, [[u, v], [t, vt]])

# A really cool comparison of the simulated vs analytic solution:
#dt = 0
#while np.max(u) > 3.0:
#    t = t + DT/4 * u
#    u = solve(u, DL, DT)
#    dt += DT
#print(dt)
#
#v = ana(x, y, dt, 2, 2)
#vplot(x, y, [[u,v]])

# A really cool plot of the vibrational modes of heat eq. solution:
#ul = [[0,0,0],[0,0,0],[0,0,0]]
#for n in range(3):
#    for m in range(3):
#        ul[n][m] = _ana(x, y, 0.1, n+1, m+1)
#vplot(x, y, ul)
