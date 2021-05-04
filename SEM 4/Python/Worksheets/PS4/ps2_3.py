import numpy as np


# function to compute euclidean distance and return it
def euclidean_dist(p, q):
    # p and q are converted to nd arrays
    p = np.array(p)
    q = np.array(q)
    # Returns norm of p-q vector
    dist = np.linalg.norm(p - q)
    return dist


# function to compute cosine of the angle between u,v and return it
def cosine_angle(p, q):
    # unit vector = u/|u|
    # np.linalg.norm(x) returns norm of the vector
    unit_vector_p1 = p / np.linalg.norm(p)
    unit_vector_p2 = q / np.linalg.norm(q)
    # dot product of |u|,|v|
    dot_product = np.dot(unit_vector_p1, unit_vector_p2)
    angle = np.arccos(dot_product)
    return angle


# function to compare cosine and euclidean distance values of the vectors
def compare(a, b):
    if a == b:
        print("The values are equal")
    else:
        print("The values are not equal")


if __name__ == "__main__":

    n = int(input("Enter n value - "))
    # get input of u and v vectors after n value is known
    print("Enter u vector : ")
    u = []
    v = []
    for i in range(0, n):
        x = int(input(''))
        u.append(x)

    print("Enter v vector : ")

    for i in range(0, n):
        x= int(input(''))
        v.append(x)

    # cos takes return value of cosine_angle function
    cos = cosine_angle(u, v)
    # euclid takes return value of euclid_dist function
    euclid = euclidean_dist(u, v)
    # prints cos value
    print("Cosine of angle between u and v : ", end="")
    print(cos)
    # prints euclid value
    print("Euclidean distance : ", end="")
    print(euclid)

    # compare cosine and euclid values
    compare(cos,euclid)



