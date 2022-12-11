def max_sum(nums):
    max = nums[0]
    sum = 0
    start = 0
    end = 0
    dem = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum %2 != 0:
            dem = i+1
            sum = 0
        if max <= sum:
            max = sum
            start = dem
            end = i
    return nums[start: end+1]
nums = [3,-2,-2,7,3,5,4,2,3,5]
nums1 = [3,2,2,4,5,6,8,3,8,4]
nums2 = [100, 12, 20, 3, 2, 20, 4, 5, 6, 8, 3, 3, 5, 80, 1, 1001, 11, 102]
print(max_sum(nums))
print(max_sum(nums1))
print(max_sum(nums2))


