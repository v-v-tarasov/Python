def sort3(a, b, c):
    i = []
    i.append(a), i.append(b), i.append(c)
    i = sorted(i)
    return i

a, b, c = input(), input(), input()
print(*sort3(a, b, c))


