# Python 3.8

# Question :
# Given a 2 dimension array matrix of 0s and 1s, count the number of islands of 1s. 
# An island is surrounded by a group of adjacent cells that are all 1s. 
# A cell can only be adjacent to each other horizontally and vertically.

# command: python <python script> <test file>
# example command: python .\codding.py .\t1

# t1  island = 1		 
# [0,    1,    0,    1,    0]
# [0,    0,    1,    1,    1]
# [1,    0,    0,    1,    0]
# [0,    1,    1,    0,    0]
# [1,    0,    1,    0,    1]

# t2  island = 1
# ['1', '1', '1', '1', '1', '1']

# t3  island = 0, since no 1 is surrouded by 1
# ['1', '1']
# ['0', '0']

# t4  island = 1, since (0,1) is surrounded by 1
# ['1', '1']
# ['0', '1']

# t5  island = 0
# ['0', '0', '0', '0']
# ['0', '0', '0', '0']
# ['0', '0', '0', '0']

# t6  island = 1
# ['1', '1', '1', '1']
# ['1', '1', '1', '1']
# ['1', '1', '1', '1']

# t7  island = 1, boundary case, a 1x1 matrix having merely 1
# [[1]] 

# t8  island = 1, a 3x3 matrix, general case, (1, 1) is surrounded by 1
# [0,    1,    0] 
# [1,    1,    1]
# [0,    1,    0]

# t9  island = 1, since (0,2), (1,1), (1,2), and (2,2) are surrounded by 1, and they are adjacent cells
# ['0', '1', '1']
# ['1', '1', '1']
# ['0', '1', '1']

# t10  island = 0
# ['1', '0', '1']
# ['0', '1', '0']
# ['1', '0', '1']

# t11  island = 2, (1,0) and (2,3) are surrounded by 1's, but they are not connected
# ['1', '0', '0', '1']
# ['1', '1', '0', '1']
# ['1', '0', '1', '1']


import sys
import argparse
 
def findIsland(binaryMatrix, visited, i, j, m, n):
    
    # since island is not 
    if(i - 1 >= 0 and binaryMatrix[i-1][j] == '0'): return 0
    if(i + 1 < m and binaryMatrix[i+1][j] == '0'): return 0
    if(j - 1 >= 0 and binaryMatrix[i][j-1] == '0'): return 0
    if(j + 1 < n and binaryMatrix[i][j+1] == '0'): return 0

    visited[i][j] = 0
    num = 1
    if (i - 1 >= 0 and binaryMatrix[i-1][j] == '1' and visited[i-1][j] == -1):
        visited[i-1][j] = 0
        num += findIsland(binaryMatrix, visited, i - 1, j, m, n)
    if (i + 1 < m and binaryMatrix[i+1][j] == '1' and visited[i+1][j] == -1):
        visited[i+1][j] = 0
        num += findIsland(binaryMatrix, visited, i + 1, j, m, n)
    if (j - 1 >= 0 and binaryMatrix[i][j-1] == '1' and visited[i][j-1] == -1):
        visited[i][j-1] = 0
        num += findIsland(binaryMatrix, visited, i, j - 1, m, n)
    if (j + 1 < n and binaryMatrix[i][j+1] == '1' and visited[i][j+1] == -1):
        visited[i][j+1] = 0
        num += findIsland(binaryMatrix, visited, i, j + 1, m, n)
    # print("island", i, j)
    return 1 if (num>0) else 0

def numOfIsland (binaryMatrix):
    m = len(binaryMatrix) # num of rows
    n = len(binaryMatrix[0]) # num of cols
    
    # visited matrix: same size of binaryMatrix, init by -1, if visited, 0
    visited = [[-1] * n] * m
    
    num_islands = 0
    for i in range (m): #row
        for j in range (n): #column
            if(binaryMatrix[i][j]=='1' and visited[i][j]==-1):
                num_islands += findIsland(binaryMatrix, visited, i, j, m, n)
                
    return num_islands 

## testing 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(type=str, action='store', dest='filename', help='input file name')
    args = parser.parse_args()
    # print(args.filename)

    matrix = []
    print("\nBinary Matrix:")
    with open(args.filename, "r") as inputdata:
        for line in inputdata.readlines():
            line = line.strip().split(" ")
            matrix.append(line)
            print(line)

    print("\nNumber of Island:",numOfIsland(matrix))

    


