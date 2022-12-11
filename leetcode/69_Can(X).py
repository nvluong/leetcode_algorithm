
from math import sqrt

def check(x):
    l, r = 0, x
    while l <= r:
        mid = int((l + r) / 2)
        print(mid)
        if (mid * mid) > x:
            r = mid - 1
        elif (mid * mid) < x:
            l = mid + 1
        else:
            return mid
    return r



print(check(8))
