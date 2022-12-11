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
    dem = 0
    flag = 0
    for j in range(1,len(li_tmp1)):
        li_tmp2 = []
        for i in li_tmp1:
            a = i[j:]
            if a not in li_tmp2:
                li_tmp2.append(a)
            else:
                flag = 1
                break
        if flag == 1:
            break
        print(li_tmp2)
        dem += 1
    print(dem)

check(li_tmp, n, m)
