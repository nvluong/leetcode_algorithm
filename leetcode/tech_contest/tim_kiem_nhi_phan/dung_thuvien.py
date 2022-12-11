import bisect

a = [1,1,2,2,2,2,3,4,5,7]
n = len(a)-1
print(a)
x = 2
first = bisect.bisect_left(a,x,0,n)  # hàm này trả về vị trí đầu tiên >= x
last = bisect.bisect_right(a,x,0,n)  # hàm này trả về vị trí đầu tiên > x
print(first)
print(last)