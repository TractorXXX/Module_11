import matplotlib.pyplot as plt
import numpy as np

# Библиотека matplotlib

# Создание простого графика
fig_1, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 2, 3, 1])
plt.show()

# Создание графиков функций
x = np.linspace(0, 6, 100)

fig_2, ax = plt.subplots(figsize=(8, 8), layout='constrained')
ax.plot(x, x, label='Линейная')
ax.plot(x, x**2, label='Квадратичная')
ax.plot(x, x**3, label='Кубическая')
ax.set_xlabel('Ось x')
ax.set_ylabel('Ось y')
ax.set_title('Графики функций')
ax.legend()
plt.show()

# Гистограмма
fig_3, ax = plt.subplots(figsize=(10, 8), layout='constrained')
categories = ['принтеры', 'ноутбуки', 'мониторы', 'камеры', 'телевизоры', 'наушники', 'телефоны']

ax.bar(categories, np.random.rand(len(categories)))
plt.show()

# Библиотека numpy

# Объединение массивов
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9]])
z = np.concatenate((x, y), axis=0)
print(z)

# Количество элементов в массиве
print('Количество элементов в массиве: ',z.size)
print()

# Сортировка массива
a = np.array([7, 3, 9, 1, 8, 2, 6, 4, 5])
print(np.sort(a))

