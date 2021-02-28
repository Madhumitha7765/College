numbers1 = [2, 7, 1, 45, -1, 134]
numbers2 = [6, 7, 13, 12, -2, 45, 45]

set1 = set(numbers1)
seta = []
set2 = set(numbers2)
setb = []

sorted(set1)
sorted(set2)

if set1 == set2:
    print('Both sets are equal')
else:
    for value in numbers1:
        if value not in numbers2:
            seta.append(value)
    for value in numbers2:
        if value not in numbers1:
            setb.append(value)

print("Elements of set A : " , end=" ")
print(seta)
print("Elements of set B : " , end=" ")
print(setb)