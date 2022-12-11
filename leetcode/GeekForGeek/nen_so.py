

a = [10,50,20,40,30] #-> 0,4,1,3,2
def convert(a):
    tmp = a[:]
    tmp.sort()
    print(tmp)
    dict = {}
    val = 0
    for i in range(len(tmp)):
        dict[tmp[i]] = i
    print(dict)

convert(a)