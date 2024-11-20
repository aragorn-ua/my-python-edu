# name = 'Ira'
# age = 50
# animal = 'cat'

# print (age == 50 and 'r' in name or animal != 'dog')

lst = [1, 2, 3, 4, 5]
dct = {"name": "Tom", "age": 5}
name = "Tom"
tpl = ("n", "a", "g")

result = dct["age"] in lst
print(result)

result = dct["age"] in lst and dct["name"] in tpl
print(result)

check = None

print(dct["name"] == name and dct["age"] in lst)

# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
str = ''
print (type(str))
num_int = 1 #integer
num_float = 1.2 #
yes_or_no = True
some_list = ['some','list']
print (type(num_float))
print (type(str))
print (type(yes_or_no))
print (type(some_list))
some_obj = {'name': 'Vova', 'age': 35}
print (type(some_obj))
some_tuple=('some',4,'tuple')
print (type(some_tuple))
some_none = None
print (type(some_none))
# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
print (num_int > num_float )
print (num_float == yes_or_no)
# 3. Використати вивчені функції Python:
# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
num_str = str(num_str)
#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
# усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
message = message.replace ('y','0').replace('i','1')
print (message)
#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
text=split_test.split(' ')
print (text)
string_join=' '.join(text)
print (string_join)

#  4. Визначити довжину рядку string_join за допомогою функції len()
print(len(string_join))

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)
#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print(list_extend.index(6))
#  4. Визначити довжину списку list_append за допомогою функції len()
print(len(list_append))
# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'],dict_test['where'])
#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print("Keys:", list(dict_test.keys()))
print("Values:", list(dict_test.values()))
#  3. За допомогою функції items() вивести на екран пари ключ - значення
print(list(dict_test.items()))


# Initial dictionary
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154),
            'Germany': (357114, 83783942)}
# Update dictionary with two countries
countries_dict["Brazil"] = (8515767, 212559417)
countries_dict["India"] = (3166391, 1380004385)
print(len(countries_dict))
print(countries_dict.items())