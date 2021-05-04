def ispangram(str):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabets:
        if char not in str.lower():
            return False
    return True

string = input('Enter the string : ')
if ispangram(string):
    print('Sentence is a Pangram')
else:
    print('Sentence is not a Pangram')