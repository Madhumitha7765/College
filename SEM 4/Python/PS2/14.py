def removeduplicates(numbers):
    set1 = set(numbers)
    return list(set1)


numbers = [2, 7, 1, 45, 45, 45, 1, 8]
print(removeduplicates(numbers))