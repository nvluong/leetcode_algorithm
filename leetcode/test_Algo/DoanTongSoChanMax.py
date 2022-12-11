def max_sum(nums):
    r = 0
    n = len(nums)
    sum = 0
    max = 0
    temp_r = 0
    temp_l = 0
    dem = 0
    dem1 = 0
    while r <= n - 1:
        if nums[r] % 2 == 0:
            sum += nums[r]
            dem += 1
            dem1 += 1
            if r == n - 1:
                if max <= sum:
                    temp_r = r
                    temp_l = r - dem + 1
                    if temp_l != temp_r:
                        max = sum
        else:
            if r - 1 >= 0 and nums[r - 1] % 2 == 0:
                if max <= sum:
                    max = sum
                    a = temp_l
                    b = temp_r
                    temp_r = r - 1
                    temp_l = r - dem
                    if temp_l == temp_r:
                        temp_r = b
                        temp_l = a
            sum = 0
            dem = 0
        r += 1
    if dem1 < 2:
        print("-1")
    else:
        # print(temp_l, temp_r)
        print(nums[temp_l: temp_r+1])
    print(max)

nums = [3,-2,-2,7,3,5,4,2,3,5]
nums1 = [3,2,2,4,5,6,8,3,8,4]
nums2 = [100, 12, 20, 3, 2, 20, 4, 5, 6, 8, 3, 3, 5, 80, 1, 1000, 10, 100]
nums3 = [10, 12, 20, 3, 2, 20, 4, 5, 6, 8, 3, 3, 5, 80, 1, 1001, 11, 102]
max_sum(nums)
max_sum(nums1)
max_sum(nums2)
max_sum(nums3)


