def primetest(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

for i in range(1,50):
    if primetest(i):
        print(i)