class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_le = []
        list_chan = []
        for i,num in enumerate(nums):
            if i % 2 == 0:
                list_chan.append(num)
            else:
                list_le.append(num)
        list_chan.sort()
        list_le.sort(reverse=True)
        j = 0
        k = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = list_chan[j]
                j+=1
            else:
                nums[i] = list_le[k]
                k+=1
        return nums



sol = Solution()
nums = [4,1,2,3]
print(sol.sortEvenOdd(nums))