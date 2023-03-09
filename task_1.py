import numpy as np
import time
from random import uniform

t_start = time.perf_counter()  # обозначаем время начала работы

s1 = np.random.uniform(1, 10 ** 10, 1000001)  # создаем два массива, заполненные миллионом случайных чисел
s2 = np.random.uniform(1, 10 ** 10, 1000001)
result = np.multiply(s1, s2)  # выполняем операцию поэлементного перемножения массивов

# # аналогично для стандартных массивов без использования numpy
# s1, s2, result = [uniform(1, 10 ** 10) for i in range(1000001)], [uniform(1, 10 ** 10) for j in range(1000001)], []
# for i in range(1000001):
#     result.append(s1[i] * s2[i])

print(time.perf_counter() - t_start)  # печатаем время работы алгоритма
