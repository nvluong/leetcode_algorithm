# li = list(map(int, input().split()))
# n = li[0]
# m = li[1]
# li_tmp = []
# for i in range(n):
#     str = input()
#     li_tmp.append(str)
# print(li_tmp)
li_tmp = ['qwpt', 'abcf', 'bvoa', 'abka', 'bbhb']
n = 5
m = 4
li_tmp1 = []
def check(li_tmp, n, m):

    for i in range(m):
        s = ""
        for j in range(n):
            s+=li_tmp[j][i]
        li_tmp1.append(s)
    print(li_tmp1)
    print("------------------")
    li = []
    for i in li_tmp1:
        li.append(i[::-1])
    li.sort()
    print(li)
    k = 0
    min_tmp = 1000
    for i in range(m-1):
        for j in range(n):
            if li[i][j] != li[i+1][j]:
                if j == 0:
                    break
                k = n-j-1
                print(li[i], li[i+1])
                print("j", j)
                print("k ", k)
                min_tmp = min(min_tmp, k)
                print("min ", min_tmp)
                break
    return min_tmp




print(check(li_tmp, n, m))
