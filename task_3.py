import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.use('TkAgg')
fig = plt.figure(figsize=(7, 4))
ax = Axes3D(fig)
# ax = fig.add_subplot(projection='3d')
pi = np.pi
x = np.linspace(-5*pi, 5*pi)
y = np.cos(x)
z = np.sin(x)
ax.plot(x, y, z, color='darkblue')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
fig.suptitle('График функции:', fontsize=14)
plt.show()
