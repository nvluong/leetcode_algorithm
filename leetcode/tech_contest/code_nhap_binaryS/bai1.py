a = [2,1,4,3,6,5,11]
c = 11
def check(a,c):
    """
    cách này truyeenf thống giống trong sách
    :param a:
    :param c:
    :return:
    """
    a.sort()
    print(a)
    l = 0
    r = len(a)-1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == c:
            return mid
        elif a[mid] >= c:
            r = mid - 1
        else:
            l = mid + 1
    return -1

print(check(a,c))
