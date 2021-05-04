import numpy as np


# transpose of matrix
def transpose(matrix,tr,N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = matrix[j][i]

# function that checks if matrix is Symmetric
def isSymmetric(matrix,N):
    tr = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    transpose(matrix,tr,N)
    for i in range(N):
        for j in range(N):
            if(matrix[i][j] != tr[i][j]):
                return False

    return True


# function that checks if matrix is Stochastic
def isStochastic(matrix,N):
    matrix = np.array(matrix)
    for x in matrix:
        if(float(sum(x)) == 1.0):
            if all(0 <= y <= 1.0 for y in x) is False:
                return False
            else:
                return False

    return True


# function that checks for orthogonality of matrix
def orthogonal(matrix):
    matrix = np.array(matrix)
    res1 = np.dot(matrix,matrix.T)
    res2 = np.dot(matrix.T,matrix)

    if idendity(res1) and idendity(res2):
        return True

    return False


# function that returns identity of matrix
def idendity(matrix):
    n = len(matrix)
    matrix = np.array(matrix)

    return np.allclose(np.identity(n),matrix)


if __name__ == '__main__':
    N = int(input('Enter the number of rows '))
    matrix = []

    for i in range(N):
        a = []
        for j in range(N):
            a.append(int(input()))
        matrix.append(a)

    # check if matrix is symmetric,orthogonal,stochastic and print the result
    if isSymmetric(matrix,N):
        print('Symmetric : Yes')
    else:
        print('Symmetric : No')

    if isStochastic(matrix, N):
        print('Stochastic : Yes')
    else:
        print('Stochastic : No')

    if orthogonal(matrix):
        print('Orthogonal : Yes')
    else:
        print('Orthogonal : No')

