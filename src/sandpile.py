# Contains various utilities for working with sandpiles and toppling vectors.
import numpy as np

# Topples a toppling vector into its corresponding sandpile.
def topple(v):
    v = np.pad(v, ((1, 1), (1, 1)))
    l = np.roll(v, -1,  axis=1)
    r = np.roll(v, 1, axis=1)
    u = np.roll(v, -1, axis=0)
    d = np.roll(v, 1, axis=0)

    return (l + r + u + d - v*4)[1:-1, 1:-1]

# True if the given sandpile is stable.
def isStable(u):
    return np.min(u) >= 0 and np.max(u) < 4

# True is the given sandpile is legal, i.e. every weight is positive.
def isLegal(u):
    return np.min(u) >= 0

# Topples the given sandpile until it's stable.
def stabilise(_u):
    u = np.copy(_u)
    v = zero(u.shape[0], u.shape[1]) # toppling vector

    # First we make u legal by removing any negative weights:
    while not isLegal(u):
        dv = np.clip(u // 4, None, 0)
        v += dv
        u += topple(dv)

    # Then we make u stable by collapsing large vertices:
    while not isStable(u):
        dv = u // 4
        v += dv
        u += topple(dv)

    return u, v

# Returns the zero grid.
def zero(width, height):
    return np.zeros((width, height), dtype=int)

# Returns the uniformly one grid.
def one(width, height):
    return np.ones((width, height), dtype=int)

# Returns the identity element of the recurrence group.
def identity(width, height):
    fst, _ = stabilise(one(width, height) * 8)
    res, _ = stabilise(one(width, height) * 8 - fst)
    return res
