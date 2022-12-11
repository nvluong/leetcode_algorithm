a = [1,2,3,3,5,6,3,4]
k = 3
def check_first(a, k):
    a.sort()
    print(a)
    l = 0
    r = len(a)-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if a[mid] >= k:
            ans = mid
            r = mid-1
        else:
            l = mid+1
    return ans
print(check_first(a,k))

def check_last(a,k):
    l = 1
    r = len(a)
    ans = -1
    while l<= r:
        mid = (l+r)//2
        if a[mid] <= k:
            l = mid+1
            ans = mid
        else:
            r = mid-1
    return ans
print(check_last(a,k))