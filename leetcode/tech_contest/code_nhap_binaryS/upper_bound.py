a = [1,1,2,6,15, 20, 23]
c = 16

def check(a,c):
    """
    tìm mid nhỏ nhất mà a[mid] >= c
    :param a:
    :param c:
    :return:
    """
    l = -1
    r = len(a)
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
    r = len(a)
    b = -1
    while l < r:
        mid = (l+r)//2
        if a[mid] >= c:
            b = mid
            r = mid
        else:
            l = mid+1
    return b
print(cach_2(a,c))

def cach_3(a,c):
    l = 0
    r = len(a)
    b = -1
    while l < r:
        mid = (l+r)//2
        if a[mid] >= c:
            b = mid
            r = mid
        else:
            l = mid+1
    return b
print(cach_3(a,c))