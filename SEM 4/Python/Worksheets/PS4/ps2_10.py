# function for counting number of digits of a positive integer
def count_digits(n):
    if n == 0:
        return 1
    # digit count is stored in r variable
    r = 0
    # while loop iterates until number/10 become less than 1
    while n:
        n = n/10
        r += 1
        if n < 1:
            break
    return r


if __name__ == '__main__':
    n=int(input("Enter number : "))
    print("The number of digits are : ",end="")
    print(count_digits(n))
