a = int(input())
b = 10 ** a - 1
c = 10 ** (a - 1) - 1
print(*range(b, c, -2))
