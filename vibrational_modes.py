#!/usr/bin/env python3
# Renders the vibrational modes of the analytic solution to the heat equation
# over a square domain with fixed-0 boundary conditions and an initial
# condition of constant heat.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

N = 100 # grid size
DL = 0.1 # grid spacing
L = N*DL # domain length
T = 0.16 # time for rendered solution
K = 4.0 # initial condition

x, y = np.meshgrid(
    np.linspace(0, N*DL, N+1, dtype=float),
    np.linspace(0, N*DL, N+1, dtype=float)
)

ul = [[0,0,0],[0,0,0],[0,0,0]]
for n in range(3):
    for m in range(3):
        ul[n][m] = a._heat(x, y, T, n+1, m+1, K, L)
p.plots(x, y, ul)
