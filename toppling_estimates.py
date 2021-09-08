#!/usr/bin/env python3
# Compares actual toppling vectors for constant initial conditions to the
# analytic estimates that come from solutions to the heat equation.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

K = 4 # the initial condition
L = 80 # domain length

# Get actual toppling vector.
_, v = s.stabilise(s.one(L, L) * K)
x, y = np.meshgrid(
    np.linspace(0, L, L, dtype=float),
    np.linspace(0, L, L, dtype=float)
)

# Compute analytic estimates of the toppling vector.
avgs = []
bs = np.linspace(2.5, 4.0, 20, dtype=float)
for b in bs:
    t = n.stable_time(K, L, b) # 3.5 seems to be the magic number?
    av = a.topple(x, y, t, 15, 15, K, L)
    avgs.append(np.sum(np.abs(v-av)) / L / L)

p.plot2d(bs, avgs)
