# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1,6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesdsay', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')


# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = "Hello my name is ", first_name, last_name

print(greeting)
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old")
# Desired output: I am 36 years old

print("I work as a {}.".format("profession"))
# Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for {} years.".format(
    years_experience)
print(exp_string.format())
# Desired output: I have worked in the field for 5 years.

print(f"I started in the field when I was " +
      (str(age - years_experience)) + " years old.")
# Desired output: I started in the field when I was 31 years old.
