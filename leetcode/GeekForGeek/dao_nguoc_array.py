
a = [1,2,3,4,5,5,4]

def two_pointer(a):
    l = 0
    r = len(a)-1
    while l <= r:
        a[l], a[r] = a[r], a[l]
        l+=1
        r-=1
    print(*a, sep=" ")
two_pointer(a)
a1 = [1,2,3,4,5,5,4]

def cach_2(a1):
    b = a1[::-1]
    print(b)

cach_2(a1)

