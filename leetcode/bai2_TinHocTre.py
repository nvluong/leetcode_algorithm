import math


def check(n):
    n_tmp = n
    if n <= 10:
        return 0
    end = n % 10
    flag = 0
    print(n)
    print(end)
    s = 0
    dem = 0
    if end != 9:
        while n != 0:
            a = n%10
            if dem == 0:
                a+=1
                s = s*10+a
                print("s", s)
                dem = 1
            else:
                if a == 0:
                    s = s * 10 + a
                else:
                    print("n =", n)
                    n = n-1
                    break
            n = int(n / 10)
    else:
        while n != 0:
            a = n % 10
            if a == 9 and flag == 0:
                s = s * 10 + a
                print("S2", s)
            else:
                flag = 1
                if dem == 0:
                    print("s", s)
                    a += 1
                    s = s * 10 + a
                    dem = 1
                else:
                    if a == 0:
                        s = s * 10 + a
                        print("S1", s)
                    else:
                        print("n ", n)
                        n-=1
                        break
            n = int(n / 10)
    k = n*(10**(int(math.log(s,10)+1)))+s
    print("k", k)
    len_k = int(math.log(k, 10))+1
    print(len_k)
    len_n = int(math.log(n_tmp,10))+1
    print(len_n)
    if k >= n_tmp or len_k != len_n:
        return 0
    return k

print(check(245))
