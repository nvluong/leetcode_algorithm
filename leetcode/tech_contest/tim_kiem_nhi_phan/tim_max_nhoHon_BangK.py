a = [1,2,3,9,8,2]
k = 1
def check(a, k):
    """
    tìm giá trị nhỏ nhất >= k
    """
    a.sort()
    print(a)
    l = 0
    r = len(a) -1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if a[mid] <= k:
            l = mid+1
            ans = mid
        else:
            r = mid-1
    return ans

print(check(a,k))

def check_2(a,k):
    """
    tìm giá trị bé nhất > k
    """
    a.sort()
    l = 0
    r = len(a) - 1
    while l < r - 1:
        mid = (l+r)//2
        if a[mid] >= k:
            r = mid
        else:
            l = mid
    return r
print(check_2(a,k))