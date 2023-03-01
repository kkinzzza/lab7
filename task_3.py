import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.use('TkAgg')

fig = plt.figure()  # создаем фигуру
ax = Axes3D(fig)  # создаем трехмерную систему координат 
# ax = fig.add_subplot(projection='3d')  # альтернативный метод создания 3-хмерной СК
x = np.linspace(-5*np.pi, 5*np.pi)  # интервалы согласно условию задачи
y = np.cos(x)  # задаем функциональные зависимости для осей y и z
z = np.sin(x)
ax.plot(x, y, z, color='darkblue')  # строим трехмерный график по заданию
ax.set_xlabel('x')  # указываем названия осей
ax.set_ylabel('y')
ax.set_zlabel('z')
fig.suptitle('График функции:', fontsize=14)  # указываем заголовок
plt.show() 
