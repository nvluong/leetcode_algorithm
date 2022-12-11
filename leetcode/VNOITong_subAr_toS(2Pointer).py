#
# def check(a, s):
#     left = 0
#     right = 0
#     tong = 0
#     while left > right:
#         if left != right:
#             for i in range(left, right):
#                 tong += a[i]
#             if tong > s:
#                 left+=1
#             elif tong == s:
#                 print(left, right)
#                 left+=1
#                 right+=1
#             else: right +=1
#
#
#
a=[10,2,6,2,2,6,10,2]
s = 20
l = 0
r = 0
sum = 0
asn = 0
max = 0
a1 = 0
b1 = 0
while r <= len(a) - 1:
    sum +=a[r]
    while sum > s:
        sum -= a[l]
        l+=1
    long = r-l+1
    if max < long:
        max = long
        a1 = l
        b1 = r
    r+=1
print(a1, b1)
