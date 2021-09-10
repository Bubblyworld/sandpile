#!/usr/bin/env python3
# Attempting to use the analytic solutions to the heat equation as an initial
# estimate for toppling of constant initial conditions.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

K = 4 # the initial condition
L = 1000 # domain length
P = 3.5 # continous stability threshold
C = ['red', 'green', 'blue', 'purple'] # image colours

x, y = np.meshgrid(
    np.linspace(0, L, L, dtype=float),
    np.linspace(0, L, L, dtype=float)
)

# Get stable time and an initial guess for the toppling vector.
t = a.stable_time(K, L, P)
v0 = a.topple(x, y, t, 10, 10, K, L).astype(int)
u0 = s.one(L, L) * K + s.topple(v0)

u, v = s.stabilise(u0)
p.image(u, C).show()

# I have a feeling that the discrepancies we're seeing are because there are
# two sandpiles in a given equivalence class... one of which is transient, but
# can be reached by negative topplings. Or basically the problem is that an
# equivalence class has loads of members, many of which may be stable, but
# only one of which is recurrent. Need to figure out how to tell...
