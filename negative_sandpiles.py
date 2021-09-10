#!/usr/bin/env python3
# Runs some tests to ensure that the sandpile library works even when given
# sandpiles with negative values. This is guaranteed to be sound, since one
# can show that the recurrent sandpiles form a group isomorphic to Zn^2/DZn^2,
# where D is the Laplacian of the nxn grid graph.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

def run(u, label):
    print("Case [%s]:" % (label))
    print(u)
    us, vs = s.stabilise(u)
    print("stable sandpile:")
    print(us)
    print("toppling vector:")
    print(vs)
    print("sanity check sandpile:")
    print(us == (u + s.topple(vs)))
    print("---")

# Trivial 2x2 case.
u2 = s.zero(2, 2)
u2[1, 1] = -1
run(u2, "2x2 trivial")

# Trivial 3x3 case.
u3 = s.zero(3, 3)
u3[1, 1] = -1
run(u3, "3x3 trivial")
