
a = 124
i = 2
while a > 1:
    if a % i == 0:
        print(i)
        a//=i
    else:
        i+=1
