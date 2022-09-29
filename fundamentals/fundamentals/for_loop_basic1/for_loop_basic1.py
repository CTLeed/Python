for ii in range(151):
    print(ii)

for ii in range(5, 1001, 5):
    print(ii)

for ii in range(1, 101):
    if ii % 10 == 0:
        print("Coding Dojo")
    elif ii % 5 == 0:
        print("Coding")
    else:
        print(ii)

# sum = 0
# for ii in range(0, 500001):
#     if ii % 2 == 1:
#         sum += sum + ii

# print(sum)

for ii in range(2018, 0, -4):
    print(ii)

lowNum = 2
highNum = 9
mult = 3
for ii in range(lowNum, highNum + 1):
    if ii % mult == 0:
        print(ii)
