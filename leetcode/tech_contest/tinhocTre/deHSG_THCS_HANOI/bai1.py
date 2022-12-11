import math
def check(a,b,mod):
    res = 0
    a = a % mod
    b = b % mod
    print(int((a*b)%mod))
li = list(map(int,input().split()))
a = li[0]
b = li[1]
c = li[2]
li_1 = [a,b,c]
li_1.sort()
a1 = li_1[1]
b1 = li_1[2]
c1 = li_1[0]
m = li[3]
if a1 > 0:
    check(a1,b1,m)
else:
    check(c1,a1,m)
