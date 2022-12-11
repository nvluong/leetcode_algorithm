
def swap(a,b):
    temp = a
    a = b
    b = temp


def sinh_HoanVi(nums):
    n = len(nums)
    index = -1
    for i in reversed(range(n-1)):
        if nums[i] < nums[i+1]:
            index = i
            break
    i = n -1
    while i >= 0 and index != -1:
        if nums[i] > nums[index]:
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp
            break
        i-=1
    print("idex", index)
    l = index+1
    print("l = ", l)
    r = n - 1
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l+=1
        r-=1
    return nums



a = [5,2,1]
print(sinh_HoanVi(a))
