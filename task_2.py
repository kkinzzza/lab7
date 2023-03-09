import matplotlib
import numpy as np
import csv
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

time, throttle_valve, fuel_consumption = np.array([]), np.array([]), np.array([])  # создаем массивы для соотв. значений
with open('data1.csv', encoding='utf8') as file:  # открываем файл, указывая кодировку
    file_reader = csv.reader(file, delimiter=';')  # считываем данные из файла
    next(file_reader)  # необходимо, чтобы не записывать первую строку с заголовками
    for row in file_reader:  # считываем данные и записываем их в массивы
        time = np.append(time, float(row[0]))
        throttle_valve = np.append(throttle_valve, int(row[3]))
        fuel_consumption = np.append(fuel_consumption, float(row[17]))
    fig = plt.figure()  # создаем окно
    ax1 = plt.subplot(121)  # добавляем систему координат для графика, в скобках указываем позицию в окне
    ax1.plot(time, throttle_valve, time, fuel_consumption)  # создаем графики зависимостей параметров от времени
    ax1.grid()  # на систему координат накладываем сетку
    ax1.set_xlabel('Время', fontsize=10)  # подписываем оси
    ax1.set_ylabel('Значение параметра: \n синий - положение дроссельной заслонки, \n '
                   'оранжевый - часовой расход топлива', fontsize=10)
    # далее - аналогично
    ax2 = plt.subplot(122)
    ax2.scatter(throttle_valve, fuel_consumption, color='pink', edgecolor='darkblue')  # создаем график корреляции
    ax2.grid()
    ax2.set_xlabel('Положение дроссельной заслонки', fontsize=10)
    ax2.set_ylabel('Часовой расход топлива', fontsize=10)
fig.suptitle('Графики зависимостей положения дроссельной заслонки \n '
             'и часового расхода топлива от времени \n'
             'и график их корреляции:')
plt.show()  # команда необходима для показа окна с графиками
