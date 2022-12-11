
nums = [4,8,1,2]

def check(nums):
    n = len(nums)-1
    flag = 0
    s = 0
    while n >= 0:
        if flag == 0:
            s+=pow(nums[n],2)
            flag = 1
        else:
            s-= pow(nums[n], 2)
            flag = 0
        n-=1
    print(s)
check(nums)
