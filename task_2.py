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
    ax1 = plt.subplot(221)  # добавляем систему координат для графика, в скобках указываем позицию в окне
    ax1.plot(time, throttle_valve, color='red')  # создаем график зависимости положения дрос. засл. от времени
    ax1.grid()  # на систему координат накладываем сетку
    ax1.set_xlabel('Время', fontsize=9)  # подписываем оси
    ax1.set_ylabel('Положение дроссельной заслонки (%)', fontsize=9)
    # далее - аналогично
    ax2 = plt.subplot(222)
    ax2.plot(time, fuel_consumption, color='orange')
    ax2.grid()
    ax2.set_xlabel('Время', fontsize=9)
    ax2.set_ylabel('Часовой расход топлива (л/час)', fontsize=9)
    ax3 = plt.subplot(212)
    ax3.scatter(time, throttle_valve, color='darkblue')  # с помощью метода scatter создаем точечный график корреляции
    ax3.scatter(time, fuel_consumption, color='green')
    ax3.grid()
    ax3.set_xlabel('Время', fontsize=10)
    ax3.set_ylabel('Значение параметра: \n синий - положение дроссельной заслонки, \n '
                   'зеленый - часовой расход топлива', fontsize=9)
    fig.suptitle('Графики зависимости положения дроссельной заслонки \n и '
                 'часового расхода топлива от времени', fontsize=14)  # записываем заголовок окна
    plt.show()  # команда необходима для показа окна с графиками
