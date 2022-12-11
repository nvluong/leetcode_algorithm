


mod = pow(10, 9)+7
base = 311
n = 5
m = 4
li_tmp = ['qwpt', 'abcf', 'bvoa', 'abka', 'bbhb']
def hash(a, mod, base):
    li = []
    li[0] = (ord(a[0]) - ord('a'))%mod
    for i in range(1,len(a)):
        s = (li[i-1]*base + (ord(a[i]) - ord('a'))%mod ) %mod
        li.append(s)
    return li

def check(li_tmp, n, m, mod, base):
    li = []
    for i in range(m):
        s = ""
        for j in range(n):
            s+=li_tmp[j][i]
        li.append(s)

    print(li)
check(li_tmp, n, m, mod, base)