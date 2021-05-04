# 19PW13
c=int(input("Enter the number of patients : "))

for i in range(1,c+1):
    dict = {}
    print("\nPATIENT ",i)
    while True:
        name = input('Enter patient name :')
        if any(x.isdigit() for x in name):
               print("Enter valid name")
               continue
        else:
            break
    """while True:
        gender = str(input('Enter patient gender :'))
        if str(gender.lower())=="female" or str(gender.lower())=="male":
               break
        else:
            print("Enter valid gender")
            continue"""
    gender=str(input("Enter gender : "))
    date_of_birth=str(input("Enter DOB [dd/mm/yyyy] : "))
    address=str(input("Enter address : "))
    weight=int(input("Enter weight : "))
    symptoms=input("enter symptoms separated by comma : ")
    a = tuple(str(x) for x in symptoms.split(","))
    print(a)
    n=int(input("Enter the number of tests taken so far : "))
    for i in range(1,n+1):
        test_name=input("Enter the test name : ")
        test_result=input("Enter test result : ")
        dict[test_name]=test_result
    print(dict)
    # tests (as a dictionary, with test_name as the key, and the test_result as the value).
    Dengue_normal_ranges={"IgM ratio":1.2,"HI":1280,"Platelet count":100000}
    count=0
    test=0
    for x in dict.keys():
         for y in Dengue_normal_ranges.keys():
             if x==y=="IgM ratio":
                 if float(dict[x])>float(Dengue_normal_ranges[y]):
                     count=1
                     test = 1
             if x == y == "HI":
                 if int(dict[x]) > int(Dengue_normal_ranges[y]):
                     count = 2
                     test = 1
             if x == y == "Platelet count":
                 if int(dict[x]) < int(Dengue_normal_ranges[y]):
                     count = 3
                     test = 1

         if(count==3):
             print("Tested positive for dengue")
             break
         elif count ==0 :
             print("Insufficient info for conclusion")
             break






