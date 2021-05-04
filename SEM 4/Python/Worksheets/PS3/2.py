# function to find max value of the input list
def get_max(int_list):
    if len(int_list) == 1:
        return int_list[0]
    else:
        # recursive call to get_max function till end of int_list
        max = get_max(int_list[1:])
        # maximum element is returned by comparing max variable and int_list[0]
        if max > int_list[0]:
            return max
        else:
            return int_list[0]

# driver code


if __name__ == "__main__":
    # creating an empty list
    lst = []
    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    print("Enter the numbers in the list : ")
    for i in range(0, n):
        element = int(input())
        lst.append(element)  # adding the element

    print("The maximum element is ", end=" ")
    # print the return value of get_max function
    print(get_max(lst))
