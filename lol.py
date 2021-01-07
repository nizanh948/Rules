import numpy as np 
import random 
def lol(matrix):
    # get the data 
    # a subset of letters 
    lis = ['a', 'b', 'c']
    matrix = [[0,0,1], [0,1,0], [1,0,0]] # 000 no edge it only picks up once , # 010 it it produces an infinte loop , # 
    x = random.randint(0, len(matrix)-1)
    for row in range(3): # outer loop as many times as wanted: so after the third time theres only one loop 
        for col in range(len(matrix[0])):
            if matrix[x][col] == 1:
                print("x is ", x, "col is ", col)
                next = random.choice([x, col])
                print("next is ", next)
                x = next 
                print("row becomes", x)
                # the issue if the coloum has no matchs the first time ?
            # after this ?
lol([[0,0,1], [0,1,0], [1,0,0]])
lis = ['a', 'b', 'c']


