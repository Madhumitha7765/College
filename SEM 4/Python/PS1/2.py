websites = []
count = int(input('Enter number of websites : '))

for i in range(0, count):
    s1 = input('Enter website URL :  ')
    websites.append(s1)

for website in websites:
    s1 = website.split('.')
    print(s1[2])