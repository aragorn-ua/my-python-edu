# -*- coding: utf-8 -*-
import os
import sys

# Переключаем стандартный вывод на UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Assign starting number (counter)
i = 1

# While loop will print all the numbers to 10
while i < 10: # Condition
  print(i, end = ' ') # Action
  i = i + 1 # Increasing variable
print("\n")
  # List from previous tasks
people = ["Alex", "Noah", "Peter", "John", "Michelle"]
# Use for loop to iterate over list
for i in people:
  print(i)

  # Range with three arguments
for i in range(0, 20, 2):
  print(i, end = ' ')
print("\n")
  # Use for loop to print numbers from 10 to 20 squared
for i in range (10,21):
  print(i**2, end = ' ')

  # Initial list
values = [1, [2, 3], 4, "code"]

# Initialize a for loop over indexes
for i in range(len(values)):
  print("Index:", i)
  print("Value:", values[i])
  print("----") # Delimiter

  # Countries data
countries = [['USA', 9629091, 331002651], ['Canada', 9984670, 37742154],
['Germany', 357114, 83783942], ['Brazil', 8515767, 212559417], ['India', 3166391, 1380004385]]


# Iterate over list
for country in countries:
  # Iterate over nested list
  for j in country:
    print(j, end = ' ')
  print('\n') # Print new line after nested loop finish


  ### Умовні конструкції:

# 1. **Перевірка паролю:**
#    Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
native_password = 'password123'
user_password = 'password123'
if user_password == native_password:
  print ('Ви увійшли в систему')
else: print ('Неправильний пароль')

# 2. **Визначення днів тижня:**
#    Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
day_number = 8
days_of_week = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}

if day_number >= 1 and day_number <=7:
    print(f"День тижня: {days_of_week[day_number]}")
else:
    print("Помилка: Номер дня недійсний. Будь ласка, введіть число від 1 до 7.")
# ### Цикли:

# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.

for user_num in range(1,10,1):
  j = 0
  print('\n')
  print(f"Таблиця множення для {user_num}:")
  while j <=10:
    print(user_num*j, end = ' ')
    j += 1
# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.
num_list = [1, 42, 56, 86, 9, 23]
sum_list = 0
for num in num_list:
    sum_list += num
print(sum_list)

# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.
user_number = 0
factorial = 1

for i in range (1,user_number+1):
  factorial *=i
print (f"Факторіал числа {user_number} дорівнює {factorial}")
# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.
for par in range (1,51):
  if par%2==0: print (par)
# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
end = 20
start = 2
for user_num in range(start, end + 1):
    is_prime = True

    for i in range(2, user_num):
        if user_num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f'Число {user_num} - просте')



# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`. Використовуйте умовні конструкції і цикли для розв'язання кожного завдання. Бажаю успіхів у виконанні цих завдань!
