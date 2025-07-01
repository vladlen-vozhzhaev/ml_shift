# name = input("What is your name? ")
# print("hello "+name)
# a = input("Enter a number: ")
# b = input("Enter b number: ")
# print(a + b)
# login = input("Enter your login: ")
# password = input("Enter your password: ")
# if login == "admin" and password == "123":
#     print("You are logged in")
# elif login == "user" and password == "321":
#     print("You are logged in")
# else:
#     print("You are not logged in")
# numbers = [1, 2, 3, 4, 5]
#
# for number in numbers:
#     print(number)
# for char in "Python":
#     print(char)
# for i in range(2,10):
#     print(i)
# i = 1
# while i<=5:
#     print(i)
#     i += 1
# for number in range(10):
#     if number % 2 == 0:
#         continue
#     print(number)
# for number in range(10):
#     if number == 7:
#         break
#     print(number)
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
# my_list = [1, 2, 3]
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# my_list[0] = 6
# print(my_list)
# my_list.append(8)
# print(my_list)
# my_list.insert(1, 9)
# print(my_list)
# my_list.remove(9)
# print(my_list)
# num = my_list.pop(0)
# print(num, my_list)
my_string = "Hello WORLD! "
first_char = my_string[0]
print(first_char)
last_char = my_string[-1]
print(last_char)
substring = my_string[6:11]
print(substring)
if "Hell" in my_string:
    print("Hell, найден")
else:
    print("Hell, не найден")

print(my_string.upper())
print(my_string.lower())
print(my_string.title())
print(my_string.strip())
print(my_string.split())
print("https://vozhzhaev.ru/taskBank/python".split("/"))
original_string = "I like apples"
new_string = original_string.replace("apples", "oranges")
print(new_string.find("like"))
print(len(new_string))
path1 = "C:\\Users\\Student\\AppData"
print(path1)
my_string = """lorem ipsum dolor sit amet"""