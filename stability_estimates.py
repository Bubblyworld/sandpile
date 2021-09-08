#!/usr/bin/env python3
# Comparisons between analytic estimates of stability time, numeric estimates
# of stability time, and actual data on stability time for the sandpile.
import numpy as np
import src.sandpile as s
import src.plots as p
import src.analytic as a
import src.numeric as n

NL = [i*20 for i in range(1, 10)] # grid sizes
K = 4.0 # initial condition

for N in NL:
    print("Case N=" + str(N) + ":")

    ### Numeric estimate
    x, y = np.meshgrid(
        np.linspace(0, N, N+1, dtype=float),
        np.linspace(0, N, N+1, dtype=float)
    )
    
    t_num = 0
    u = np.ones((N+1, N+1), dtype=float) * K
    v = np.zeros((N+1, N+1), dtype=float)
    while np.max(u) > 3.0:
        t_num += 1.0
        u, v = n.heat(u, v, 1.0, 1.0)
    ###

    ### Analytic estimate
    t_ana = a.stable_time(K, N)
    ###
    
    print("  numerical stability time: " + str(t_num))
    print("  analytic estimate: " + str(t_ana))
