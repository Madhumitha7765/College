# Consider an n-digit number k.
# Square it
# add the right n digits to the left n or n-1 digits.
# If the resultant sum is k,
# then k is called a Keprekar number.
def iskeprekar(n):
    square = n * n
    length = len(str(n))
    string = str(square)
    right = int(string[-1*length:])
    left = int(string[:-1*length])
    if right+left == n:
        return True
    else:
        return False


num = int(input("Please enter the number: "))
if iskeprekar(num):
    print("This is a keprekar number")
else:
    print("This is not a keprekar number")