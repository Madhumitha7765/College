list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
numbers = []

for value in list1:
    if value in list2:
        numbers.append(value)

print(numbers)