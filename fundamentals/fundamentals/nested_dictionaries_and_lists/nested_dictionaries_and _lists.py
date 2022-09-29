# 1 Update Values in Dictionaries and Lists

x = [
    [5, 2, 3],
    [10, 8, 9]
]
print(x)
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
print(students)
students[0]["last_name"] = "Bryant"
print(students)

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory)
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z = [{'x': 10, 'y': 20}]
print(z)
z[0]["y"] = 30
print(z)

# 2 Iterate Through a List of Dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for ii in range(0, len(students)):
        for key, val in students[ii].items():
            print(key, "-", val)


iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for ii in range(0, len(some_list)):
        print(some_list[ii][key_name])


iterateDictionary2("first_name", students)


# 4 Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, list in some_dict.items():
        print(len(list), key.upper())
        for value in list:
            print(value)
        print("")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']


}
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
