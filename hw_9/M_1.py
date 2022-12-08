import csv
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print('time: ',time.time() - start_time)
        return res
    return wrapper

def read_matrix (file):
    matrix = []
    with open (file) as f:
        matrix = [list(map(int, row.split(';'))) for row in f.readlines()]
    return matrix

def stroka_na_stolbec(row,column):
    res = 0
    for i in range (len(row)):
        res += row[i] * column[i]
    return res

@time_decorator
def multiplication (A,B):
    l = len(A)
    n = len(B[0])
    res =[[0]*n for _ in range(l)]
    for i in range (l):
        for j in range (n):
            row = A[i]
            column = []
            for x in range(len(B)):
                column.append(B[x][j])
                
            res[i][j] = stroka_na_stolbec(row,column)
    return res

A = read_matrix ('A.txt')
B = read_matrix ('B.txt')
    
print(multiplication (A,B))     


