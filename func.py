# def sayHello(name):
#     print(f"Hello {name}")
#
# sayHello("Alex")
# sayHello("Ivan")
# sayHello("Oleg")
#
# def f(x, c, y=2):
#     return x**y + c
#
# print(f(x=5, c=1))
# print(f(-6, 3, 1))

# def sum_numbers(*numbers, d):
#     summ = 0
#     for n in numbers:
#         summ += n
#     print(summ)
#
# sum_numbers(1,2,3,4,5, d=2)
# sum_numbers(1,2,3, d=1)

# x = 10 # global
#
# def change_x():
#     global x
#     x = 20 # global
#     y = 40 # local
#
# change_x()
# print(x)

# f = lambda x: x**2
# print(f(5))

# def my_decorator(func):
#     def wrapper():
#         print("До функции")
#         func()
#         print("После фукнции")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello")
#
# say_hello()

# Задача: реализовать функцию, которая принимает в качестве параметра сумму,
# которую необходимо отдать пользователю в виде чисел (монет) 1, 2, 5, 10. DRY
# def getChange(num):
#     coin = 0
#     if num >= 10: coin = 10
#     elif num >= 5: coin = 5
#     elif num >= 2: coin = 2
#     elif num >= 1: coin = 1
#
#     if coin > 0:
#         print(coin)
#         getChange(num - coin)

# def getChange(num):
#     coin = 10 if num >= 10 else 5 if num >= 5 else 2 if num >= 2 else 1 if num >= 1 else 0
#     if coin > 0:
#          print(coin)
#          getChange(num - coin)
#
# getChange(32)

# def f(n):
#     if n>2:
#         return f(n-1)+f(n-2)
#     else: return n
#
# print(f(5))

# f(4)+f(3) = 5 + 3 = 8
# f(3)+f(2) = 3 + 2 = 5
# f(2)+f(1) = 2 + 1 = 3

# marks = [3,3,4,4,5]
# summ = 0
# for mark in marks:
#     summ += mark
#
# print(summ/len(marks))
# Найти максимальный нечётный элемент списка
# numbers = [-3222,-435,-34,-236,-342,-53]
# max = float("-inf")
# for number in numbers:
#     if number > max and number % 2 != 0:
#         max = number
#
# print(max)