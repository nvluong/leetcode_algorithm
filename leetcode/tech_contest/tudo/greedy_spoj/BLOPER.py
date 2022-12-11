li = list(map(int, input().split()))
n = li[0]
s = li[1]

def check(n, s):
    sum_all = (n*(n+1))/2
    flag = [0]*(n+10)
    for i in reversed(range(1,n+1)):
        if sum_all - 2*i >= s:
            flag[i] = 1
            sum_all -= 2*i
    if sum_all == s:
        if flag[1] == 1:
            for i in range(4,n+1):
                if flag[1] == 0:
                    break
                if flag[i] == 1:
                    for j in range(2, (i//2)+1):
                        if flag[j] == 0 and flag[i+1-j] == 0:
                            flag[j] = flag[i+1-j] = 1
                            flag[1] = flag[i] = 0
                            break
            if flag[1] == 1:
                return "Impossible"
                # print('Impossible')
        s = "1"
        for i in range(2,n+1):
            if flag[i] == 1:
                s += "-" + str(i)
            else:
                s += "+" + str(i)
        # print(s)
        return s
    else:
        # print('Impossible')
        return "Impossible"

print(check(n,s))