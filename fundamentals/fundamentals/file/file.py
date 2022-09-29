num1 = 42  # - variable declaration /Number data type (integer)
num2 = 2.3  # - variable declaration /Number data type (float)
boolean = True  # - variable declaration  /Boolean data type
string = 'Hello World'  # - variable declaration /String data type
# initialized list of strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# initialized dictionary of strings, integers, and booleans
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
# initialized tuple of strings
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # log statement of type check
print(pizza_toppings[1])  # log statement of accessed value of list
pizza_toppings.append('Mushrooms')  # add value to list
print(person['name'])  # log statement of accessed value of dictionary
person['name'] = 'George'  # change value of dictionary
person['eye_color'] = 'blue'  # change value of dictionary
print(fruit[2])  # log statment of accessed value of tuple

# if/else conditional
if num1 > 45:  # if condition
    print("It's greater")  # log statement
else:  # else condition
    print("It's lower")  # log statement

# if/else if/else conditional
if len(string) < 5:  # if condition of string length
    print("It's a short word!")  # log statment
elif len(string) > 15:  # else if condition of string length
    print("It's a long word!")  # log statement
else:  # else codition
    print("Just right!")  # log statement

# for loop
for x in range(5):  # start at 0, stop at 5
    print(x)  # log statment of index
for x in range(2, 5):  # start at 2, stop at 5
    print(x)  # log statement of index
for x in range(2, 10, 3):  # start at 2, stop at 10, step of 3
    print(x)  # log statement of index
x = 0  # assign new value to x
while (x < 5):  # while loop, start at 0, stop at 5
    print(x)  # log statement of index
    x += 1  # step of 1

pizza_toppings.pop()  # delete last value of list
pizza_toppings.pop(1)  # delete 2nd value of list

print(person)  # log statment of dictionary
person.pop('eye_color')  # delete key of dictionary
print(person)  # log statment of dictionary

# for loop containing if conditionals
for topping in pizza_toppings:  # iterate through each value of list
    if topping == 'Pepperoni':  # if condition
        continue  # continue to iterate
    print('After 1st if statement')  # log statement
    if topping == 'Olives':  # if codition
        break  # break loop

# define function


def print_hello_ten_times():  # no parameters
    for num in range(10):  # for loop start at 0, stop at 9
        print('Hello')  # log statement


# function call
print_hello_ten_times()

# define function


def print_hello_x_times(x):  # parameter
    for num in range(x):  # for loop start at 0, stops at x
        print('Hello')  # log statement


# function call with arguement passed
print_hello_x_times(4)

# define function


def print_hello_x_or_ten_times(x=10):  # parameter
    for num in range(x):  # for loop start at 0, stop at 10
        print('Hello')  # log statement


# function call with no argument
print_hello_x_or_ten_times()
# function call with argument
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'
