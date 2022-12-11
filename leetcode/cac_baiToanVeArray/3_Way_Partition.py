# a = [6, 9, 11, 3, 8, 5,6,3,2,1,8, 19, 21]
a = [0,2,2,1,2,0,0,2,1,1]
end = len(a) -1
begin  = 0
l = 1
h = 2
for i in range(len(a)):
    if a[i] < l:
        tmp = a[i]
        a[i] = a[begin]
        a[begin] = tmp

        begin+=1
    elif a[i] > h:
        print("haha")
        print(a[i])
        print(a[end])
        tmp1 = a[i]
        a[i] = a[end]
        a[end] = tmp1
print(a)