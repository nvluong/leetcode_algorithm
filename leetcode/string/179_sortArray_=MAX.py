
# a = [0, 10, 1, 99, 9, 8, 79, 91, 22, 32, 12]
a = [1, 10, 11]

class Solution:
    def largestNumber(self, nums):

        print("núm", nums)
        str_nums = [str(num) for num in nums]
        print(str_nums)
        str_nums.sort()
        b = str_nums[::-1]
        print("b ", b)
        l = len(b)
        for i in range(len(b)):
            for j in reversed(range(i, l)):
                if b[i] + b[j] < b[j] + b[i]:
                    b[i], b[j] = b[j], b[i]
        s = ""
        for i in b:
            s+=i
        return s

sol = Solution()
# nums = [3,30,34,5,9]
print(sol.largestNumber(a))


