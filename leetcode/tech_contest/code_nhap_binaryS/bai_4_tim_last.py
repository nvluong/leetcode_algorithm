a = [1,1,1,2,2,2,3,3,3,4]
c = 1
def check(a,c):
    """
    cách này trong sách
    :param a:
    :param c:
    :return:
    """
    l = 0
    r = len(a)-1
    while l<= r:
        mid = (l+r)//2
        if ((mid == r or a[mid+1] > c) and a[mid] == c):
            return mid
        elif a[mid] <= c:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(check(a,c))

def cach_2(a,c):
    """
    cachs này của topcoder
    :param a:
    :param c:
    :return:
    """
    l = -1
    r = len(a)-1
    while l < r - 1:
        mid = (l+r)//2
        if a[mid] <= c:
            l = mid
        else:
            r = mid
    return l
print(cach_2(a,c))

def cach_3(a,c):
    """
    tu nghĩ

    :param a:
    :param c:
    :return:
    """
    l = 0
    r = len(a)-1
    b = -1
    while l<=r:
        mid = (l+r)//2
        if a[mid] <= c:
            l = mid + 1
            b = mid
        else:
            r = mid - 1
    return b
print(cach_3(a,c))