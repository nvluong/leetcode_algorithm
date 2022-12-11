
a = [1,1,2,2,2,2,3]
def check(a, c):
    l = 0
    r = len(a)-1
    b = 0
    while l<= r:
        mid = (l+r)//2
        if mid == c:
            b = mid
            r = mid-1
        else:
            l = mid+1
    print(b)
check(a, 2)