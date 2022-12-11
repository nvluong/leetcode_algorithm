

def check(n,s):
    dem = 0
    for i in range(0, n+1):
        if s - i <= 2*n and s-i >= 0:
            if s - i >= n :
                dem+= 2*n - (s - i) + 1
            else:
                dem+=s-i+1
    return dem

li = list(map(int, input().split()))
n = li[0]
s = li[1]
print(check(n, s))