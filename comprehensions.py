"""
List, Dictionary, and Set comprehension

1 line loops
"""






### Basic example
# Lets say we have a list of strings that we want to convert to ints

my_line = ['0', '1', '2', '10', '100']

# # Here is the long way, using a for loop
# new_line = []
# for x in my_line:
#     x = int(x)
#     new_line.append(x)
# print(new_line)  # [0, 1, 2, 10, 100]


# # Here is the short way, using list comprehension
# new_line = [int(x) for x in my_line]
# print(new_line)  # [0, 1, 2, 10, 100]


# another example, lets assume we have read lines in a CSV file into a list
my_lines = ['fruit,flavor,convenience,durability\n', 'banana,5,5,2\n', 'apple,3,4,5\n', 'grapes,4,4,2\n', 'lemon,1,3,4\n', 'orange,3,3,3\n', 'watermelon,4,1,5\n', 'tomato,2,2,1']

# # the old way to process each line
# new_lines = []
# for x in my_lines:
#     x = x.strip().split(',')
#     new_lines.append(x)
# print(new_lines)

# # the new way
# new_lines = [x.strip().split() for x in my_lines]
# print(new_lines)



## Timing
import time

# # lets make the list bigger so we can measure it
# my_lines = my_lines*100000
#
# t0 = time.time()
#
# new_lines = []
# for x in my_lines:
#     new_lines.append(x.strip().split(','))
#
# t1 = time.time()
# print("for loop:{}".format(t1-t0))
#
# t0 = time.time()
# new_lines = [x.strip().split() for x in my_lines]
# t1 = time.time()
# print("list comp:{}".format(t1-t0))




## List comprehension with an IF statement (The "IF" goes at the end)

numbers = [0, 1, 2, 3, 10, 11, 12, 13]

# # Here is the long way, using a for loop
# new_line = []
# for x in numbers:
#     if x > 7:
#         new_line.append(x)
# print(new_line)


# # Here is the short way, using list comprehension
# new_line = [x for x in numbers if x > 7]
# print(new_line)




## List comprehension with IF and ELSE statements (The "IF/ELSE" goes in the middle)
numbers = [0, 1, 2, 3, 10, 11, 12, 13]

# # Here is the long way, using a for loop
# new_line = []
# for x in numbers:
#     if x > 7:
#         new_line.append(x)
#     else:
#         new_line.append(-1)
# # print(new_line)


# # Here is the short way, using list comprehension
# new_line = [x if x > 7 else -1 for x in numbers]
# # print(new_line)




## You can use both an IF/ELSE in the middle, and an IF at the end
# my_line = ['0', '1', '2', '10', '100', 0, 1, 2, 3, 10, 11, 12, 13]
# my_line = [x if x > 7 else -1 for x in my_line if type(x) == int]
# print(my_line)




## There is no ELIF, but you can chain IF/ELSE -- this is usually a bad idea due to poor readability
# my_line = ['0', '1', '2', '10', '100', 0, 1, 2, 3, 10, 11, 12, 13]
# my_line = [x if type(x) is str else -1 if x > 7 else 7 for x in my_line]
# print(my_line)  # can you guess what will be printed without running the code?


# # the long form
# my_line = ['0', '1', '2', '10', '100', 0, 1, 2, 3, 10, 11, 12, 13]
# new_line = []
# for x in my_line:
#     if type(x) == str:
#         new_line.append(x)
#     else:
#         if x > 7:
#             new_line.append(-1)
#         else:
#             new_line.append(7)
# print(new_line)




## Dictionary comprehension
my_lines = [['banana', '5', '5', '2'], ['apple', '3', '4', '5'], ['grapes', '4', '4', '2'], ['lemon', '1', '3', '4'], ['orange', '3', '3', '3'], ['watermelon', '4', '1', '5'], ['tomato', '2', '2', '1']]

# # the long way
# fruit_to_taste = {}
# for x in my_lines:
#     fruit_to_taste[x[0]] = x[1]
# print(fruit_to_taste)

# # the short way
# fruit_to_taste = {x[0]: x[1] for x in my_lines}
# print(fruit_to_taste)




## Set comprehension
my_lines = [['banana', '5', '5', '2'], ['apple', '3', '4', '5'], ['grapes', '4', '4', '2'], ['lemon', '1', '3', '4'], ['orange', '3', '3', '3'], ['watermelon', '4', '1', '5'], ['tomato', '2', '2', '1']]

# # the long way
# fruits = set()
# for x in my_lines:
#     fruits.add(x[0])
# print(fruits)

# # the short way
# fruits = {x[0] for x in my_lines}
# print(fruits)




### Advanced List Comprehension Techniques!

## Code is run, even if result is not saved
# Bug or feature?
my_line = ['0', '1', '2', '10', '100']
# list1 = []
# list1 = [list1.append(int(x)) for x in my_line]  # REMEMBER: .append() returns None
# print(list1)


# [print(int(x)) for x in my_line]



## Creating lists of a size
# zeros = [0 for _ in range(100)]  # Underscore "_" is used when the variable name should not be accessed

#this is the same as
# zeros = []
# for _ in range(100):
#     zeros.append(0)



# This can also be used to create 2d arrays ( a list containing lists )
# i = 3
# j = 5
# table = [[0 for _ in range(i)] for _ in range(j)]
# [print(row) for row in table]
# table is technically:
# [[0, 0, 0],
# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]



## Using Join, Split and Function calls

# def can_be_int(i):
#     try:
#         int(i)
#         return True
#     except:
#         return False
#
# my_string = "A,1,B,2,C,3,4,5,6"
# numbers = ''.join([x for x in my_string.split(',') if can_be_int(x)])
# print(numbers)  # 123





## Files in list comprehension


# # reading a file inside of list comp
# fasta_file = "../04_file_types/data/fasta_example.fasta"
# headers = [line for line in open(fasta_file) if line.startswith(">")]
# print(headers)


# writing a file inside of list comp - REMEMBER: .write() returns None
my_lines = [['banana', '5', '5', '2'], ['apple', '3', '4', '5'], ['grapes', '4', '4', '2'], ['lemon', '1', '3', '4'], ['orange', '3', '3', '3'], ['watermelon', '4', '1', '5'], ['tomato', '2', '2', '1']]

# # the CORRECT way
# with open('example.txt', 'w') as outfile:
#     x = [outfile.write(','.join(line) + '\n') for line in my_lines]
# print(x)


# the WRONG way
# [open('example2.txt', 'a').write(','.join(line) + '\n') for line in my_lines]  # this will open and close the file with every iteration of the loop

