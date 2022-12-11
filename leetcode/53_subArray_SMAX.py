
def maxSubArraySum(a, size):
    max = a[0]
    sum = 0
    for i in range(0, size):
        if sum < 0:
            sum = 0
        sum = sum + a[i]
        if (max < sum):
            max = sum


    return max
a = [2,-2]

print( maxSubArraySum(a, len(a)))