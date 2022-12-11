nums = [-2, -3, 4, -1, -2, 1, 5, -3]
max = 0
sum1 = 0
for i in range(len(nums)):
    sum1+=nums[i]
max = sum1
print("max ", max)
sum = 0

for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum+= nums[j]
    for k in reversed(range(i, len(nums))):
        if max <= sum:
            max = sum
        if k != i:
            sum -= nums[k]

print("max", max)

