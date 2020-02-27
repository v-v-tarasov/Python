def reverseMinMax(i):
    maxc = i.index(max(i))
    minc = i.index(min(i))
    i[maxc], i[minc] = i[minc], i[maxc]
    return i

a = list(map(int, input().split()))
print(*reverseMinMax(a))