a = [4, 2, 7, 3, 1, 6, 0, 8, 9,5]


pivot = a[len(a)-1]
i = -1
for j in range(len(a)-1):
    if pivot >= a[j]:
        i+=1
        tmp = a[j]
        a[j] = a[i]
        a[i] = tmp
tmp = a[i+1]
a[i+1] = a[len(a)-1]
a[len(a)-1] = tmp


print(a)