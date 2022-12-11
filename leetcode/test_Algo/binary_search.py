def binary_searh(nums, val):
    l = 0
    r = len(nums) - 1
    res = 0
    while l <= r:
        mid = int(l + (r-l)/2)
        if val == nums[mid]:
            return mid

        elif val < nums[mid]:
            r = mid - 1
        else:
            l = mid+1
    return -1
nums = [-1,0,3,5,9,12]
val = 9
print(binary_searh(nums, val))
