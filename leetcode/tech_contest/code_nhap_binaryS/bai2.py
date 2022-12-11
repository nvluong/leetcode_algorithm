a = [2,1,4,3,6,5,11]
c = 11
def check(a,c):
    """

    :param a:
    :param c:
    :return:
    cachs này thì l = -1 để tìm nửa đoạn (l:r] để ko bị mất số ở đầu, cụ thể ở đây là số 1
    nếu để l = 0 thì sai
    và khoảng cách l và r ko được trùng nhau để tránh lặp vô hạn
    """
    a.sort()
    print(a)
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
