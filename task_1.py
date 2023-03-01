import numpy as np
import time
import random

t_start = time.perf_counter()  # обозначаем время начала работы
for i in range(1000001):
    s1 = np.array(random.uniform(1, 10 ** 10), float)
    s2 = np.array(random.uniform(1, 10 ** 10), float)  # создаем массивы из 1 млн случайных чисел

print(np.multiply(s1, s2))  # печатаем результат работы функции np.multiply()
print(time.perf_counter() - t_start)  # печатаем время работы алгоритма
