i=list(input().split())
min=1000
for b in range(len(i)):
    s=int(i[b])
    if (s<min)and(s>0):
        min=s
print(min)