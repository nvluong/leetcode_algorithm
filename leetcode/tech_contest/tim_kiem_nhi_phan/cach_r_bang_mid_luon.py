a = [1,2,2,2,3]
k = 2
def check_first(a, k):
    a.sort()
    print(a)
    l = -1
    r = len(a)-1
    while l < r-1:
        mid = (l+r)//2
        if a[mid] <= k:
            l = mid
        else:
            r = mid
    return l
print(check_first(a,k))