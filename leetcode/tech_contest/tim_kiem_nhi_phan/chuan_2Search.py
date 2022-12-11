

a = [2,3,1,1,9,2,6,8,10]
c = 9
def check_c1(a,c):
    """
    cach nay chuan theo sach

    """
    a.sort()
    print(a)
    l = 0
    r = len(a)-1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == c:
            return mid
        elif a[mid] < c:
            l = mid+1
        else:
            r = mid-1
    return -1
print(check_c1(a,c))
