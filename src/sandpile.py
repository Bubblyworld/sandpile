import numpy as np

# An abelian sandpile instance on a rectangular grid.
class Sandpile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # grid is padded on all sides with sink vertices
        self.grid = np.zeros((width+2, height+2), dtype=int) 

    # Returns the identity element of the critical group.
    def identity(width, height):
        fst = Sandpile(width, height)
        fst.vadd(fst.const(8))
        fst.stabilise()

        res = Sandpile(width, height)
        res.vadd(res.const(8))
        res.vadd(-fst.rgrid())
        res.stabilise()

        return res

    # Returns the reduced grid with no sink vertices.
    def rgrid(self):
        return self.grid[1:self.width+1, 1:self.height+1]

    # Returns a constant sand vector.
    def const(self, n):
        return np.ones((self.width, self.height), dtype=int) * n

    # Adds the given amount of sand to the given vertex.
    def add(self, x, y, amount):
        self.grid[1+x, 1+y] += amount

    # Adds the given vector to the sand grid.
    def vadd(self, amounts):
        self.grid[1:self.width+1, 1:self.height+1] += amounts

    # Topples sand n times at the given position.
    def topple(self, x, y, n):
        self.grid[1+x, 1+y] -= 4*n
        self.grid[2+x, 1+y] += n
        self.grid[0+x, 1+y] += n
        self.grid[1+x, 2+y] += n
        self.grid[1+x, 0+y] += n

    # Topples sand according to the given toppling vector.
    def vtopple(self, v):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.topple(x, y, v[x, y])

    def stable(self):
        return np.min(self.rgrid()) >= 0 and np.max(self.rgrid()) < 4

    def stabilise(self):
        while not self.stable():
            self.vtopple(self.rgrid() // 4)
