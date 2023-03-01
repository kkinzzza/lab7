import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib

matplotlib.use('TkAgg')

fig = plt.figure()
ax = fig.add_subplot()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.001)
y = np.sin(x)
line = plt.plot(x, y)
ax = plt.axis([-2 * np.pi, 2 * np.pi, -1, 1])
dot, = plt.plot([0], [np.sin(0)], 'ro')


def func(i):
    dot.set_data(i, np.sin(i))
    return dot,


animation = FuncAnimation(fig, func, frames=np.arange(-2 * np.pi, 2 * np.pi, 0.1), interval=20, repeat=False)
writer = PillowWriter(fps=30)
animation.save("sin_function.gif", writer=writer)
