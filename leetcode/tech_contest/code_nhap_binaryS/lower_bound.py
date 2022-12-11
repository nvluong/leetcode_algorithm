a = [1,1,2,2,15,17,20]
c = 17
def check(a,c):
    """
    tìm mid lớn nhất mà a[mid] nhỏ hơn hoặc bằng c
    cachs cua topcoder
    :param a:
    :param c:
    :return:
    """
    l = -1
    r = len(a)
    while l < r-1:
        mid = (l+r)//2
        if a[mid] <= c:
            l = mid
        else:
            r = mid
    return l
print(check(a,c))

def cach_2(a,c):
    """
    bigO
    tư tưởng cách làm này là dịch l lên 1 đơn vị cho tới khi gặp đuợc mid thỏa mãn
    mỗi lần kiểm tra thì r = mid để rút ngắn lại đoạn cần tìm

    lưu ý cách này l < r

    :param a:
    :param c:
    :return:
    """
    l = 0
    r = len(a)
    b = -1
    while l < r:
        mid = (l+r)//2
        if a[mid] >= c:
            b = mid
            r = mid
        else:

            l = mid + 1
    return b
print(cach_2(a,c))


