
start = [14,5,8,3,0,1,5,9]
end =   [18,7,9,4,6,2,9,12]

def sort_1(start, end):
    for i in range(len(end)):
        for j in range(i+1,len(end)):
            if end[i] > end[j]:
                t = end[i]
                end[i] = end[j]
                end[j] = t

                t = start[i]
                start[i] = start[j]
                start[j] = t
    return start, end
def check(start, end):
    start, end = sort_1(start, end)
    print(start)
    print(end)

    i = 0
    li = []
    li.append(1)
    for j in range(1,len(end)):
        if end[i] <= start[j]:
            print(start[i], end[i])
            i = j
            li.append(j+1)
    print(li)
check(start, end)


