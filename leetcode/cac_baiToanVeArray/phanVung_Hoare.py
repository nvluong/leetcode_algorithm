
a = [10,3,8,4,2,7,1,10]

l = 0
r = len(a)-1
pivot = a[l+2]
i = l
j = r
while (True):

    # while a[i] < pivot:
    if a[l] < pivot:
        l+=1
    # while a[j] > pivot:
    if a[r] > pivot:
        r-=1
    if l >= r :
        print(r)
        break
    print(a[l], a[r])
    tmp = a[l]
    a[l] = a[r]
    a[r] = tmp
    print(a)
print(l, r)