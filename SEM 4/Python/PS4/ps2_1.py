def check_print():
    for n in range(1, 101):
        # case : n is multiple of both 5 and 3
        if n % 5 == 0:
            if n % 3 == 0:
                print("FizzBuzz")
        # case : n is multiple of 5 only
        elif n % 5 == 0:
            print("Buzz")
        # case : n is multiple of 3 only
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)


if __name__ == "__main__":
    check_print()
