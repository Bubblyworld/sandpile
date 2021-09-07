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

# Generating solutions of the dissipation equation on the unit square:
#   4u_t = u_xx + u_yy
# ...subject to various boundary conditions, like u=0 or the more complex
#    ODE constraints I managed to scrounge from the discrete model.
#N = 100
#I = 4
#DL = 1.0
#DT = 1.0 # stability issues, should be order of mag smaller than DL

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
