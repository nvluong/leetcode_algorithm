

n = 5
c = 3
T = 4
a = [5,8,3,10, 7]

def binary(n,c,T, a):
    def check(mid):
        s = 0
        dem = 0
        for i in range(n):
            s+=a[i]
            if a[i] > mid*T:
                return False
            if s > mid*T:
                s = a[i]
                dem+=1
        if s != 0:
            dem+=1
        if dem > c:
            return False
        else:
            return True
    l = -1
    r = int(sum(a)/T)
    while l < r-1:
        mid = (l+r)//2
        if check(mid):
            r = mid
        else:
            l = mid
        # print(r)
    return r
print(binary(n,c,T, a))