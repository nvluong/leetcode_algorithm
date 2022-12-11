

def gcd(a,b):
    while a*b != 0:
        if a > b:
            a%=b
        else:
            b%=a
    return a+b
def check(n, d, k):
    return n/(d/gcd(d,k))

n =20
k = 5
d = 1
print(check(n,d,k))
