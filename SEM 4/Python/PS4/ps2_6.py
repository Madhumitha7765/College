import numpy as np


# function to find inverse of a matrix
def inverse_matrix(matrix):
    A = np.array(matrix)
    print(np.linalg.inv(A))


if __name__=="__main__":

    R = int(input("Enter the number of rows:", end=""))
    C = int(input("Enter the number of columns:", end=""))

    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(C):  # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    # For printing the matrix
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end=" ")
        print()
    X=np.array(matrix)
    inverse_matrix(X)

