# Contains utilities for computing analytic solutions to the heat equation
# on a square domain with Dirichlet boundary conditions. Can be used to 
# estimate toppling vectors for constant-height sandpiles, which I'm hoping
# will speed up their toppling time massively.
import numpy as np

# Central-difference approximation of u_xx, where dl is the cell size. This
# assumes the fixed-0 boundary condition on the grid.
def dxx(u, dl):
    u = np.pad(u, ((1, 1), (1, 1))) 
    ul = np.roll(u, -1, axis=1)
    ur = np.roll(u, 1, axis=1)
    return (ul + ur - 2*u)[1:-1, 1:-1] / dl / dl

# Central-difference approximation of u_yy, where dl is the cell size. This
# assumes the fixed-0 boundary condition on the grid.
def dyy(u, dl):
    u = np.pad(u, ((1, 1), (1, 1))) 
    uu = np.roll(u, -1, axis=0)
    ud = np.roll(u, 1, axis=0)
    return (uu + ud - 2*u)[1:-1, 1:-1] / dl / dl

# Integrates u, v according to the heat equation, where dl is the cell size,
# dt is the timestep. We take u to be the sandpile and v its toppling vector.
def heat(u, v, dl, dt):
    u_prime = u + dt/4 * (dxx(u, dl) + dyy(u, dl))
    v_prime = v + dt * u/4
    return u_prime, v_prime

