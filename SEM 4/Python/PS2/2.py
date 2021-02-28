numbers = [12, 24, 35, 24, 88, 120, 155]
list = []

for i in numbers:
    if int(i) != 24:
        list.append(i)

print("List after removing 24:")
print(list)