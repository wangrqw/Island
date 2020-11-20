# Island

## Question
Given a 2 dimension array matrix of 0s and 1s, count the number of islands of 1s. 
An island is surrounded by a group of adjacent cells that are all 1s. 
A cell can only be adjacent to each other horizontally and vertically.

## Files
* script: codding.py
* test cases: t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11

## Run command
```
python codding.py <test file>
```
For example, 
```
python codding.py t1
```

## Environment
python >= 3.0

## Test case:
t1  island = 1, since (1,3)	is surrounded by 1
```
0 1 0 1 0
0 0 1 1 1
1 0 0 1 0
0 1 1 0 0
1 0 1 0 1
```

t2  island = 1, since all cells are surrounded by 1 and they are adjacent
```
1 1 1 1 1 1
```

t3  island = 0, since no 1 is surrouded by 1
```
1 1
0 0
```

t4  island = 1, since (0,1) is surrounded by 1
```
1 1
0 1
```

t5  island = 0
```
0 0 0 0 
0 0 0 0 
0 0 0 0 
```

t6  island = 1
```
1 1 1 1 
1 1 1 1 
1 1 1 1 
```

t7  island = 1, boundary case, a 1x1 matrix having merely 1
```
[[1]] 
```

t8  island = 1, a 3x3 matrix, general case, (1, 1) is surrounded by 1
```
0 1 0 
1 1 1
0 1 0
```

t9  island = 1, since (0,2), (1,1), (1,2), and (2,2) are surrounded by 1, and they are adjacent cells
```
0 1 1 
1 1 1
0 1 1
```

t10  island = 0
```
1 0 1
0 1 0
1 0 1
```

t11  island = 2, (1,0) and (2,3) are surrounded by 1's, but they are not connected
```
1 0 0 1
1 1 0 1
1 0 1 1
```
