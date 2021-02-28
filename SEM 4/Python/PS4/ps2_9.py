import cmath


# abs function
def abs(x,flag):
    if flag==1:
        if x >= 0:
            return x
        if x < 0:
            return -1*x
    else:
        return x.real


if __name__ == '__main__':
    print("1.Real number \n2.Complex number ")
    x=int(input("Enter the choice : "))

    # case if number is real
    if x == 1:
        n=int((input("Enter the number:")))
        print("The abs value is : ", end="")
        print(abs(n,1))

    # case if number is imaginary
    elif x == 2:
        x = int(input("Enter real part:"))
        y = int(input("Enter imaginary part:"))
        # complex is inbuilt function (cmath module)
        z = complex(x,y)
        print("The abs value is : ",end="")
        print(abs(z, 0))

    # in case of invalid input
    else:
        print("Invalid input! ")

