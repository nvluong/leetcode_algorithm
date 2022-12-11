a = [1,1,1,2,2,2,3,3,4,5,6,6]
c = 6
def check(a, c):
    l = -1
    r = len(a)-1
    while l < r-1:
        mid = (l+r)//2
        if a[mid] >= c:
            r = mid
        else:
            l = mid
    return r

print(check(a,c))

def cach_2(a,c):
    l = 0
    r = len(a)-1
    b = -1
    while l <= r:
        mid = (l+r)//2
        if a[mid] >= c:
            b = mid
            r = mid-1
        else:
            l = mid+1
    return b

print(cach_2(a,c))

def cach_3(a,c):
    l = 0
    r = len(a)-1
    while l <= r:
        mid = (l+r)//2
        if ((mid == l or c > a[mid-1]) and a[mid] == c):
            return mid
        elif a[mid] >= c:
            r = mid-1
        else:
            l = mid+1
    return -1
print(cach_3(a,c))