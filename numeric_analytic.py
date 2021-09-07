#!/usr/bin/env python3
# Compares analytic to numerical solutions of the heat equation over a square
# domain with fixed-0 boundary conditions and a constant initial condition.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

N = 100 # grid size
DL = 0.1 # grid spacing
DT = 0.01 # time spacing, must be ~DL^2 for numeric stability
L = N*DL # domain length
T = 0.16 # time for rendered solution
K = 4.0 # initial condition

x, y = np.meshgrid(
    np.linspace(0, N*DL, N+1, dtype=float),
    np.linspace(0, N*DL, N+1, dtype=float)
)

t = 0
u = np.ones((N+1, N+1), dtype=float) * K
v = np.zeros((N+1, N+1), dtype=float)
while np.max(u) > 3.0: # discrete stability estimate
    t += DT
    u, v = n.heat(u, v, DL, DT)

ua = a.heat(x, y, t, 5, 5, K, L)
va = a.topple(x, y, t, 5, 5, K, L)

p.plots(x, y, [[u, v], [ua, va]])
