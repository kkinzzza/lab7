import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib

matplotlib.use('TkAgg')

fig = plt.figure()
ax = fig.add_subplot()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.001)  # задаем ось x
y = np.sin(x)  # задаем функцию
plt.plot(x, y)  # построение графика
ax = plt.axis([-2 * np.pi, 2 * np.pi, -1, 1])  # ограничения
dot, = plt.plot([0], [np.sin(0)], 'ro')  # задание точки, которая в дальнейшем будет двигаться

def func(i):
    dot.set_data(i, np.sin(i))
    return dot,


animation = FuncAnimation(fig, func, frames=np.arange(-2 * np.pi, 2 * np.pi, 0.1), interval=20, repeat=False)  # задаем движение 
writer = PillowWriter(fps=30)  # параметр анимации (кол-во кадров в секунду)
animation.save("sin_function.gif", writer=writer)  # запись анимации в файл формата *.gif
