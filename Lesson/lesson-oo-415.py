def isPointInSquare(x, y):
    return 1.0 >= x >= -1.0 and 1.0 >= y >= -1.0

x = float(input())
y = float(input())

if isPointInSquare(x, y) == True:
    print('YES')
else:
    print('NO')
