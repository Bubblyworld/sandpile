# Contains utilities for computing analytic solutions to the heat equation
# on a square domain with Dirichlet boundary conditions. Can be used to 
# estimate toppling vectors for constant-height sandpiles, which I'm hoping
# will speed up their toppling time massively.
import numpy as np

# Computes analytic solution to the heat equation on an LxL grid, with fixed-0
# boundary conditions and an initial uniform state of u_0 = K. The solution's
# x, y vibrational modes are bounded by M, N respectively:
#     4u_t = u_xx + u_yy
def heat(x, y, t, N, M, K, L):
    res = np.zeros(x.shape, dtype=float)
    for n in range(1, N+1):
        for m in range(1, M+1):
            res += _heat(x, y, t, n, m, K, L)
    return res

# Computes the m,n vibrational mode of the solution.
def _heat(x, y, t, n, m, K, L):
    const = K * 16.0 / np.pi**2 / n / m * np.sin(np.pi*n/2)**2 * np.sin(np.pi*m/2)**2
    tval = np.exp(-(n*n + m*m) * np.pi**2 / L**2 / 4 * t)
    return const * tval * np.sin(n * np.pi * x / L) * np.sin(m * np.pi * y / L)

# Integrates the analytic heat equation solution to get an estimate of the
# corresponding toppling vector:
#     v_t = u/4
def topple(x, y, t, N, M, K, L):
    res = np.zeros(x.shape, dtype=float)
    for n in range(1, N+1):
        for m in range(1, M+1):
            res += _topple(x, y, t, n, m, K, L) - _topple(x, y, 0, n, m, K, L)
    return res

# Indefinite integral of heat() with respect to time.
def _topple(x, y, t, n, m, K, L):
    const = K * 16.0 / np.pi**2 / n / m * np.sin(np.pi*n/2)**2 * np.sin(np.pi*m/2)**2
    tconst = -1.0 * L**2 / (n*n + m*m) / np.pi**2
    tval = np.exp(-(n*n + m*m) * np.pi**2 / L**2 / 4 * t)
    return const * tconst * tval * np.sin(n * np.pi * x / L) * np.sin(m * np.pi * y / L)
