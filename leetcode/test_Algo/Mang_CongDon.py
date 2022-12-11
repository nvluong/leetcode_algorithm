# a = [3, -1, -4, 1, 5, 9, -2, -6]
a = [0,-3,1,1]
def check(nums):
    flag = 0
    if len(nums) == 1:
        return nums[0]
    for i in nums:
        if i > 0:
            flag = 1
    if flag == 0:
        return max(nums)
    prefSum = []
    prefSum.append(0)
    print(prefSum)
    prefMin = []
    prefMin.append(0)
    max_tmp = nums[0]
    for i in range(len(nums)):

        prefSum.append(prefSum[i]+a[i])
        print("pre sum", prefSum)
        if prefMin[i] < prefSum[i+1]:
            prefMin.append(prefMin[i])
        else:
            prefMin.append(prefSum[i+1])
        print("pre min ", prefMin)
    for i in range(len(nums)+1):
        if max_tmp <= prefSum[i] - prefMin[i]:
            max_tmp = prefSum[i] - prefMin[i]
    return max_tmp


print(check(a))

