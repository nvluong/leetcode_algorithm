def check(a, n):
    s = 0
    max_tmp = 0
    li = []
    for i in range(n):
        for j in range(n):
            if a[j][i] == 'X':
                s += 1
        if max_tmp < s:
            max_tmp = s
            li.clear()
            li.append(i+1)
        elif max_tmp == s:
            li.append(i+1)
        s = 0
    len_tmp = len(li)

    return len_tmp, max_tmp, li


n = int(input())
list_tmp = []
for i in range(n):
    b = list(map(str, input().split()))
    list_tmp.append(b)
len_tmp, max_tmp, li = check(list_tmp, n)
print(len_tmp, max_tmp)
print(*li, " ")

