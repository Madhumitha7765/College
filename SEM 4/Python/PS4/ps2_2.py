# module imported to do norm operations for distance calculation
import numpy as np


# function to compute euclidean distance and return it
def euclidean_dist(p, q):
    # p and q are converted to nd arrays
    p = np.array(p)
    q = np.array(q)
    # Returns norm of p-q vector
    dist = np.linalg.norm(p - q)
    return dist


if __name__ == '__main__':

    n = int(input("Enter n value - "))
    # get input of u and v vectors after n value is known
    print("Enter u vector : ")
    u = []
    v = []
    for i in range(0, n):
        x = int(input(''))
        u.append(x)

    print("Enter v vector : ")

    for i in range(0,n):
        x = int(input(''))
        v.append(x)

    # prints return value of euclidean_dist function
    print("The Euclidean distance is : ", end="")
    print(euclidean_dist(u, v))
