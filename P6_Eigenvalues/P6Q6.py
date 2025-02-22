import numpy as np
from normalise import normalise

A = np.array([[3,-4,1],[-4,8,-4],[1,-4,3]])

x = np.array([[1],[0],[0]])

n = 19


def find_largest_eigenvalue():
    list = [0 for i in range(n)]
    list[0] = x
    for i in range(n-1):
        list[i+1] = A.dot(list[i])

    div = list[n-1]/list[n-2]

    return round(div[0][0],3), normalise(list[-1]) 

def find_second_largest_eigenvalue():
    list = [0 for i in range(n)]
    list[0] = x
    largest_eigenvalue = find_largest_eigenvalue()
    for i in range(n-1):
        list[i+1] = A.dot(list[i])
        print(" ")
        print(list[i+1])

        list[i+1] = list[i+1] / scaled_eigenvector
        print(list[i+1])
        print(" ")

    div = list[n-1]/list[n-2]

    return round(div[0][0],3)

largest_eigenvalue, largest_eigenvector = find_largest_eigenvalue()
scaled_eigenvector = largest_eigenvector * largest_eigenvalue

print("The largest eigenvalue is", largest_eigenvalue, "and the associated eigenvector is", largest_eigenvector)
print("The seconds largest eigenvalue is", find_second_largest_eigenvalue()) #Still does not work

