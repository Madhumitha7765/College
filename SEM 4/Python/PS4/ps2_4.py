
# function that calculates and returns pythagorean triples
def pythagorean_triples():
    c = 0
    m = 2
    # while loop iterates until c reaches 100
    while c < 100:
        # checks for triplets according to constraints and prints them
        for n in range(1, m + 1):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            # loop breaks in case of undesired values
            if c > 100:
                break
            if a == 0 or b == 0 or c == 0:
                break
            print(a, b, c)
            m = m + 1


if __name__ == "__main__":
    print("The triples are : ")
    pythagorean_triples()
