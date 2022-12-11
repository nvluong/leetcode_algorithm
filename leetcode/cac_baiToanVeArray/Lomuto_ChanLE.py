# a = [10, 2, 1, 9, 5, 4, 3, 6, 7, 5, 3, 11]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = -1
for i in range(len(a) - 1):
    if a[i] % 2 == 0:
        l += 1
        tmp = a[i]
        a[i] = a[l]
        a[l] = tmp
    print(a)


print(a)
