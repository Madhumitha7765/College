import random
def GeneratePasswd(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?'
    passwd = ''.join(random.sample(characters,length))
    return passwd

if __name__ == '__main__':
    length = int(input('Enter Length of Password :'))
    print(GeneratePasswd(length))