#!/usr/bin/env python3
# Computes the elements u_k of the sandpile recurrence group, which ordinarily
# takes O(n^4) time, even if you use fancy Grobner basis stuff. My plan is to
# be stupid and just approximate the toppling vector using analytic solutions
# of the heat equation, which is the continuous version of the dynamics.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

K = 4 # the initial condition
L = 50 # domain length
C = ['red', 'green', 'blue', 'purple'] # image colours

u, v = s.stabilise(s.one(L, L) * K)
x, y = np.meshgrid(
    np.linspace(0, L, L, dtype=float),
    np.linspace(0, L, L, dtype=float)
)

p.image(u, C).show()
