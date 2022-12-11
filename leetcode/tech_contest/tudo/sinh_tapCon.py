
def check(a,b,mod):
    res = 0
    a = a % mod
    b = b % mod
    while (b):
        if (b & 1):
            res = (res + a) % mod
        a = (2 * a) % mod
        b >>= 1
    return res
li = list(map(int, input().split()))
a = li[0]
b = li[1]
c = li[2]
li_1 = [a,b,c]
print("li1", li_1)
li_1.sort()
print("li1", li_1)
a1 = li_1[1]
b1 = li_1[2]
c1 = li_1[0]
m = li[3]
if a1 > 0:
    print(check(a1,b1,m))
else:
    print(check(c1,a1,m))