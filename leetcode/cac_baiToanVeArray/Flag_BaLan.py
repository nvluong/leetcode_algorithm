a = [0,2,2,1,2,0,0,2,1,1]
r = 0
w = 0
b = len(a)-1
while w <= b:
    if a[w] == 0:
        tmp = a[w]
        a[w] = a[r]
        a[r] = tmp
        w+=1
        r+=1
    elif a[w] == 2:
        tmp = a[w]
        a[w] = a[b]
        a[b] = tmp
        b-=1
    elif a[w] == 1:
        w+=1
print(a)