import numpy as np
import matplotlib.pyplot as plt
# array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# print(array)
# matrix = np.array([[1,3], [2,4]])
# print(matrix)
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a+b)
# print(a.mean())
# arr = np.array([0,1,2,3,4,5])
# print(arr[1:4]) # [1 2 3]
# print(arr[arr>2]) # [3 4 5]
# A = np.array([[1,2], [3,4]])
# B = np.array([[5,6], [7,8]])
# print(np.dot(A,B))
# print(A @ B)
# print(np.linalg.det(A))
# print(np.linalg.inv(A))
# zeros = np.zeros((3,3))
# print(zeros)
# ones = np.ones((3,3))
# print(ones)
# random = np.random.random((3,3))
# print(random)

# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# plt.figure(figsize=(8,4))
# plt.plot(x,y, label = 'sin(x)', color = 'blue', linewidth = 2)
# plt.title('sin(x)')
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
# plt.grid(True)
# plt.legend()
# plt.show()

# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.figure(figsize=(8,4))
# plt.plot(x,y1, label = 'sin(x)', color = 'blue', linewidth = 2)
# plt.plot(x,y2, label = 'cos(x)', color = 'red', linewidth = 2)
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
# plt.grid(True)
# plt.legend()
# plt.show()

categories = ['Яблоки', 'Бананы', 'Вишни', 'Финики']
values = [15,30,5,12]

plt.figure(figsize=(7,5))
plt.bar(categories, values, color=['red', 'blue', 'green', 'yellow'])
plt.title('Продажа фруктов')
plt.ylabel('Кол-во (кг)')
plt.grid(axis='y')
plt.show()

print(plt.get())

# # Данные
# labels = ['Python', 'JavaScript', 'Java', 'C++', 'Другие']
# sizes = [45, 20, 15, 10, 10]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
#
# # Создаем круговую диаграмму
# plt.figure(figsize=(7, 7))
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal')  # Чтобы диаграмма была круглой
# plt.title('Популярность языков программирования')
# plt.show()