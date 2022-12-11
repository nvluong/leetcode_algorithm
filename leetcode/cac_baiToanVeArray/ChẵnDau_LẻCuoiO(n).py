
a = [10,2,1,4,3,5,8,9,7,0,1]

l = 0
r = len(a)-1
while l <= r:
    if a[l]%2 ==0:
        l+=1
    if a[r] %2 !=0:
        r-=1
    if l < r:
        tmp = a[l]
        a[l] = a[r]
        a[r] = tmp
    print(a)
