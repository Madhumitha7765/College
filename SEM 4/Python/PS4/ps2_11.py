if __name__ == '__main__':
    lt=[3,6,9,12,15,21,24]
    x=[]
    x.append(lt[3])
    x.append(lt[4])

    # mid elements in another list
    print("Mid elements : ",end="")
    print(x)

    # slicing mid elements from original list
    lt=lt[:3]+lt[5:]
    print("After slicing: ", end="")
    print(lt)

    # inserting using slicing
    lt[3:3]=x
    print("After inserting: ", end="")
    print(lt)