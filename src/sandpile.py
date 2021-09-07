import numpy as np

# An abelian sandpile instance on a rectangular grid.
class Sandpile:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height), dtype=int) 
        self.topplegrid = np.zeros((width, height), dtype=int)

    # Returns the identity element of the critical group.
    def identity(width, height):
        fst = Sandpile(width, height)
        fst.vadd(fst.const(8))
        fst.stabilise()

        res = Sandpile(width, height)
        res.vadd(res.const(8))
        res.vadd(-fst.grid)
        res.stabilise()

        return res

    # Returns a constant sand vector.
    def const(self, n):
        return np.ones((self.width, self.height), dtype=int) * n

    # Adds the given amount of sand to the given vertex.
    def add(self, x, y, amount):
        self.grid[1+x, 1+y] += amount

    # Adds the given vector to the sand grid.
    def vadd(self, v):
        self.grid += v

    # Returns a sand delta for the given toppling vector.
    def vtopple(self, v):
        v = np.pad(v, ((1, 1), (1, 1)))
        l = np.roll(v, -1,  axis=1)
        r = np.roll(v, 1, axis=1)
        u = np.roll(v, -1, axis=0)
        d = np.roll(v, 1, axis=0)

        return (l + r + u + d - v*4)[1:-1, 1:-1]

    def stable(self):
        return np.min(self.grid) >= 0 and np.max(self.grid) < 4

    def stabilise(self):
        cnt = 0.0
        while not self.stable():
            cnt += 1.0
            self.topplegrid += self.grid // 4
            self.grid += self.vtopple(self.grid // 4)
        return cnt
