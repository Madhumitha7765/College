import itertools


def check_metathesis_pair(word1, word2):
    # initialise empty list
    list1 = []
    list2 = []
    # checks for metathesis pair between characters of word1,word2 until length of word1
    for x in range(len(word1)):
        # case if characters of both words don't match, they are appended to 2 different lists
        if word1[x] != word2[x]:
            list1.append(word1[x])
            list2.append(word2[x])
        # checks for length and set(characters) of both lists
        # returns true if words are metathesis pairs
        if len(list2) == len(list1) and len(list1) == 2 and set(list1) == set(list2):
            return True
    # returns false if all conditions fail
    return False


# function that returns the metathesis pairs in the list
def find_metathesis_pair(inputlist):
    # initialise empty list
    res = []
    # using itertools lib,it generates all possible combinations in pairs of 2
    pairs = list(itertools.combinations(inputlist, 2))
    # checks  for metathesis pair by comparing length first ,
    # calls the check_metathesis_pair function in case of equal lengths
    for x, y in pairs:
        if len(x) == len(y):
            if check_metathesis_pair(x,y):
                # appends to res list if condition satisfied
                res.append((x,y))
    # returns res
    return res


if __name__ == '__main__':
    # initialise list
    input_list = [
        "converse", "conserve",
        "abc", "acb",
        "19pw", "19pw13"
    ]

# use this code if we need to input the string to find the methasis pair
    # length = int(input('Enter the number of words '))
    # print('Enter the words ')
    # for i in range(length):
    #     word = input(f'{i + 1} : ')
    #     inputList.append(word)


result = find_metathesis_pair(input_list)
print(result)