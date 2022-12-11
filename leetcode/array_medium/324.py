class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = nums[:]
        a.sort()
        print(a)
        if len(nums) == 1:
            return nums
        flag = 0
        mid = int(len(nums)/2)-1
        if len(nums) % 2 == 0:
            b = a[:mid+1]
            c = a[mid+1:]

        else:
            flag = 1
            b = a[:mid + 2]
            c = a[mid + 2:]
        b = b[::-1]
        c = c[::-1]
        print(b)
        print(c)

        li = []
        i = 0
        for i in range(len(c)):
            li.append(b[i])
            li.append(c[i])
        if flag == 1:
            li.append(b[i+1])
        for i in range(len(nums)):
            nums[i] = li[i]
        return nums



sol = Solution()
nums = [4,5,5,6]
print(sol.wiggleSort(nums))