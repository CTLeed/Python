# 1 Countdown
def countdown(num):
    num_list = []
    for ii in range(num, 0, -1):
        num_list.append(ii)
    return num_list


print(countdown(5))

# 2 Print and Return


def print_and_return(list):
    print(list[0])
    return list[1]


print_and_return([1, 2])
print(print_and_return([1, 2]))

# 3 First Plus Length


def first_plus_length(list):
    return (list[0] + len(list))


print(first_plus_length([1, 2, 3, 4, 5]))

# 4 Values Greater than Second


def values_greater_than_second(list):
    new_list = []
    if len(list) > 2:
        for ii in range(0, len(list)):
            if (list[ii] > list[1]):
                new_list.append(list[ii])
        print(len(new_list))
        return new_list

    else:
        return False


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

# 5 This Length, That Value


def length_and_value(size, value):
    new_list = []
    for ii in range(0, size):
        new_list.append(value)
    return new_list


print(length_and_value(4, 7))
print(length_and_value(6, 2))
