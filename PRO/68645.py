import numpy as np

def triangle(start, m):
    if m == 1:
        return np.array([[start]])
    one = list(range(start,start+m))
    two = list(range(one[-1]+1,one[-1]+m))
    three = list(range(two[-1],two[-1]+(m-1))) + [start]
    three.reverse()

    temp = np.array([[0]*m]*m)
    temp[:,0] = one
    temp[m-1,1:] = two
    np.fill_diagonal(temp,three)
    return(temp)

def fun(m): #최대값도 필요해
    return sum([i+1 for i in range(m)])

def solution(n):
    m = n
    start = 1

    row,col = 0,0

    matrix = np.zeros((n,n)).astype(int)

    while matrix.max() < fun(m):
        table = triangle(start,n)
        idx = np.tril_indices(n)
        table = table[idx]
        matrix[(idx[0]+row,idx[1]+col)] = table

        n = n-3
        start = np.max(table) + 1
        row += 2
        col += 1
    return matrix
'''
    answer = matrix[np.tril_indices(m)]
    return [int(i) for i in answer]
'''
