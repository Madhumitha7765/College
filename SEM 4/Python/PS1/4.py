string = input("Enter the string : ")
index = int(input("Enter the index : "))
char = input("Enter the character : ")

list1 = list(string)
list1[index] = char
string = ''.join(list1)
print(string)