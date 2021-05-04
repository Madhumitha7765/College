def centered_average(nums):
    small = min(nums)
    big = max(nums)
    return (sum(nums) - small - big) / (len(nums) - 2)


lst = []
n = int(input("Enter number of elements : "))
print("Enter the elements : ")
for i in range(0, n):
    x = int(input())
    lst.append(x)

a=centered_average(lst)
print(a)