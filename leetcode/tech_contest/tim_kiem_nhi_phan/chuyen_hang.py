
def check(suchua, weights, days):
    s = 0
    n = len(weights)
    days-=1
    for i in range(n):
        if s + weights[i] <= suchua:
            s+=weights[i]
        else:
            days-=1
            s = weights[i]
    return days >= 0

def binary(weights, days):
    l = 0
    r = 0
    n = len(weights)
    for i in range(n):
        l = max(l, weights[i])
        r += weights[i]
    while l < r:
        mid = (l+r)//2
        if check(mid, weights, days):
            r = mid
        else:
            l = mid+1

    return l
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(binary(weights, days))