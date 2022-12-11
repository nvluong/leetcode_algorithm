
a = [1,2,3,-1,2,5,-4,-6]


l = 0
r = len(a)-1
while l < r:
    if a[l] < 0 and a[r] < 0:
        l+=1
    elif a[l] > 0 and a[r] <0:
        tmp = a[l]
        a[l] = a[r]
        a[r] = tmp
        l+=1
        r-=1
    elif a[l] > 0 and a[r] >0:
        r-=1
    else:
        l+=1
        r-=1
    print(a)
