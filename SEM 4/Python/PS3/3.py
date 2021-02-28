# function that counts frequency of elements of the string
def base_freq(string):
    # declare empty dictionary 'frequency'
    frequency = {}
    for key in string:
        if key not in frequency:
            frequency[key] = 1
        else:
            frequency[key] += 1
    # sort the items of list based on its key in alphabetical order
    return sorted(frequency.items(), key=lambda item: item[0])


if __name__ == '__main__':
    # print result of base_freq function
    print(base_freq("AAGTTAGTCA"))
