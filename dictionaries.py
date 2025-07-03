# my_dict = {'name':'Ivan', 'age':43}
# my_dict["lastname"] = "Ivanov"
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# for key, value in my_dict.items():
#     print(f"{key} = {value}")
# print(my_dict['age'])
# print(my_dict.get('lastname', "Ivanov"))
# del my_dict['age']
# print(my_dict)
# my_dict["lastname"] = "Ivanov"
# print(my_dict)
# print(my_dict.pop('name'))
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# my_tuple = (3,1,2,3,4,3,5,3)
# print(my_tuple.count(3))
# print(my_tuple.index(3))
# print(my_tuple + my_tuple)
# print(len(my_tuple))
# print(4 in my_tuple)
# print(12 in my_tuple)
# for item in my_tuple:
#     print(item)
# my_set1 = {4,3,2,6,2}
#
# my_list = [1,2,3,4,4,5,2,5,1]
# my_set2 = set(my_list)
# print(my_set2)
# # Объединение
# print(my_set1.union(my_set2))
# print(my_set1 | my_set2)
# # Пересечение
# print(my_set1.intersection(my_set2))
# print(my_set1 & my_set2)
# # Разность
# print(my_set1.difference(my_set2))
# print(my_set1 - my_set2)
# # Симметрическая разность
# print(my_set1.symmetric_difference(my_set2))
# print(my_set1 ^ my_set2)
#
# a = {"as": "As"}
# print(isinstance(a, dict))

WordsDict={}
for iWord in range(4):
    word_= input("enter")
    len_=len(word_)
    WordsDict.setdefault(word_, len_)
    #WordsDict[word_]=len_

print(isinstance(WordsDict.items(), type(WordsDict.items())))
print(type(WordsDict.items()))