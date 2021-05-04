# function to get count of each element in the string
def most_frequent(str):
    # create dictionary frequency
    frequency = dict()
    # for loop iteration to find frequency count
    for key in str:
        # checks if element of string is present in the dictionary declared
        # frequency assigned 1 if no repetition
        # frequency count incremented for repetition
        if key not in frequency:
            frequency[key] = 1
        else:
            frequency[key] += 1
    # will sort dictionary based on the result of the lambda function in descending order and return it
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)


# driver code


if __name__ == '__main__':
    # input string from user
    string = input('Enter a string : ')
    # print the return value of most_frequent function
    print(most_frequent(string))
