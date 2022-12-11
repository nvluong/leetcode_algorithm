a = [1,2,3,2,10,12]
k = 6
def check(a,k):
    a.sort()
    print(a)
    l = 0
    r = len(a)-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if a[mid] >= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans
print(check(a,k))
def check_2(a,k):
    a.sort()
    l = 0
    r = len(a)-1
    while l < r - 1:
        mid = (l+r)//2
        if a[mid] >= k:
            r = mid
        else:
            l = mid
    return r
print(check_2(a,k))
