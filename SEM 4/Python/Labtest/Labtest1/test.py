n=int(input('Enter number of patients:'))
for i in range(0,n):
    print('Patient',i+1,' name',end="")
    patient_name=input()
    gender=input('Gender:')
    DOB=input('D.O.B')
    address=input('Address')
    symptoms=tuple(map(str,input('Symptoms').split(','))) #give input with comma like cough,sneeze,cold
    tests={}
    tests['Igm ratio']=float(input('IgM Ratio:'))
    tests['HI']=float(input('HI'))
    tests['Platelets Count']=int(input("Platelets Count:"))
    if tests['Igm ratio']<1.2 and tests['HI']<1280 and tests['Platelets Count']>100000:
        print('Patient ',i,": Dengue Negative")
    else:
        print('Patient ',i+1,": Dengue Positive")