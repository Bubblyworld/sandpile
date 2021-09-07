# Contains utilities for plotting 3d graphs, like sandpiles, heat equation
# solutions, toppling vectors and other stuff.
import matplotlib.pyplot as plt

# Plots a single graph, where x, y are meshgrids and u is the graph values.
def plot(x, y, u):
    plots(x, y, [[u]])

# Plots many graphs, where ul is a NxM grid of graph values.
def plots(x, y, ul):
    fix, axes = plt.subplots(len(ul), len(ul[0]), subplot_kw={"projection": "3d"})
    for n in range(len(ul)):
        for m in range(len(ul[0])):
            if (len(ul) == 1):
                axes[m].plot_surface(x, y, ul[n][m])
            else:
                axes[n, m].plot_surface(x, y, ul[n][m], cmap="cool")
    plt.show()
