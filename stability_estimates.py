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
    print("  numerical: " + str(n.stable_time(K, N)))
    print("  analytical: " + str(a.stable_time(K, N)))
