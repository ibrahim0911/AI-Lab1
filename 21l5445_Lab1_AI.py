#!/usr/bin/env python
# coding: utf-8

# In[1]:


# //hello program
# name = input("Please Enter Your Name: ")
# age = int(input("Enter Age: "))
# print(f"Welcome, {name}")
# print(f"You are {age} years old")

# //Data Type Identification 
# user_input = input("Enter something: ")
# try:
#     converted_input = int(user_input)
#     print(f"The data type is: {type(converted_input)} (int)")
# except ValueError:
#     try:
#         converted_input = float(user_input)
#         print(f"The data type is: {type(converted_input)} (float)")
#     except ValueError:
#         print(f"The data type is: {type(user_input)} (str)")
# //List Operations
# my_list = ['apple', 'banana', 'cherry']
# my_list.append('date')
# my_list.remove('banana')
# for item in my_list:
#     print(item.upper())
# //Tuple Unpacking 
# my_tuple = (1, 2, 3, 4)
# first, second = my_tuple[0], my_tuple[1]
# print(f"First: {first}, Second: {second}")
# //Dictionary Managment 
# students = {
#     "Alice": 90,
#     "Bob": 85,
#     "Charlie": 88,
#     "David": 92,
#     "Eva": 95
# }
# print(students)
# //Set Operations
# list1 = list(map(int, input("Enter integers for list 1 separated by spaces: ").split()))
# list2 = list(map(int, input("Enter integers for list 2 separated by spaces: ").split()))

# set1 = set(list1)
# set2 = set(list2)

# print("Union:", set1.union(set2))
# print("Intersection:", set1.intersection(set2))
# print("Difference (set1 - set2):", set1.difference(set2))
# //Conditional Statment 
# number = int(input("Enter an integer: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# //FizzBuzz
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# //Factoirial calculator 
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a non-negative integer: "))
# print(f"The factorial of {num} is {factorial(num)}")
# //Prime Number Checker 
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number to check if it's prime: "))
# print(f"{num} is prime: {is_prime(num)}")
# //List Comprehension 
# def square_numbers(numbers):
#     return [x ** 2 for x in numbers]

# nums = list(map(int, input("Enter integers separated by spaces: ").split()))
# print(square_numbers(nums))
# //Merge Dictionaries
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)
# //Remove Duplicates 
# def remove_duplicates(lst):
#     seen = []
#     return [x for x in lst if not (x in seen or seen.append(x))]

# nums = list(map(int, input("Enter integers separated by spaces: ").split()))
# print(remove_duplicates(nums))
# //Palindrome Checker
# def is_palindrome(s):
#     s = ''.join(s.split()).lower()
#     return s == s[::-1]

# string_input = input("Enter a string to check if it's a palindrome: ")
# print(f"{string_input} is a palindrome: {is_palindrome(string_input)}")
# //Fibb 
# def fibonacci(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence[:n]

# n_terms = int(input("How many Fibonacci numbers would you like? "))
# print(fibonacci(n_terms))
# //Avg Cal
# numbers = []
# while True:
#     num_input = input("Enter a number (or 'done' to finish): ")
#     if num_input.lower() == 'done':
#         break
#     try:
#         num = float(num_input)
#         numbers.append(num)
#     except ValueError:
#         print("Please enter a valid number.")

# if numbers:
#     average = sum(numbers) / len(numbers)
#     print(f"The average is: {average}")
# else:
#     print("No numbers were entered.")
# //NESTED loops 
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i * j}", end="\t")
#     print()
# //User registration system 
# users_db = {}

# def register():
#     username = input("Create a username: ")
#     password = input("Create a password: ")
#     users_db[username] = password

# def login():
#     username = input("Username: ")
#     password = input("Password: ")
    
#     if username in users_db and users_db[username] == password:
#         print("Login successful!")
#     else:
#         print("Invalid credentials.")

# register()
# login()
# //Counting  Elements
# words = input("Enter words separated by spaces: ").split()
# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)
# //Temp Converter
def convert_temperature(temp, scale):
    if scale.lower() == 'c':
        return (temp * 9/5) + 32 # Celsius to Fahrenheit
    elif scale.lower() == 'f':
        return (temp - 32) * 5/9 # Fahrenheit to Celsius

temp_value = float(input("Enter temperature value: "))
scale_choice = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ")

converted_temp = convert_temperature(temp_value, scale_choice)
if scale_choice.lower() == 'c':
    print(f"{temp_value}°C is {converted_temp}°F")
else:
    print(f"{temp_value}°F is {converted_temp}°C")






# In[ ]:




