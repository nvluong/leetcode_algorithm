#

a = 110083329
# a = 7
def check(a):
    b = str(a)
    c = a%9
    flag = 0
    s = ""
    if c == 0:
        s+=b[:1]
        s+='0'
        s+=b[1:]
    else:
        d = str(9 - c)
        for i, n in enumerate(b):
            if d < n and flag == 0:
                flag = 1
                s+=d
            s+=n
        if flag == 0:
            s+=d
    print(s)
check(a)



