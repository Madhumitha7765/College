def Intersection(setA,setB):
    return list(set(setA) & set(setB))

def Union(setA,setB):
    return set(setA).union(setB)

def Difference(setA,setB):
    return set(setA).difference(setB)

def Sym_Difference(setA,setB):
    return set(setA).symmetric_difference(setB)

n = int(input("Please enter the number of elements in the set 1: "))
setA = set()
print("Please input the set")
for _ in range(n):
    val = int(input())
    setA.add(val)
n = int(input("Please enter the number of elements in the set 2: "))
setB = set()
print("Please input the set")
for _ in range(n):
    val = int(input())
    setB.add(val)

print(f'Intersection = {Intersection(setA,setB)}')
print(f'Union = {Union(setA,setB)}')
print(f'Difference  = {Difference(setA,setB)}')
print(f'Symmetric Difference = {Sym_Difference(setA,setB)}')

