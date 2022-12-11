class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        chan = []
        le = []
        s_chan = 0
        s_le = 0
        for i, num in enumerate(nums):
            if i % 2 ==0:
                s_chan+=num
            else:
                s_le+=num
            chan.append(s_chan)
            le.append(s_le)
        print(le)
        dem = 0
        for i in range(n):
            if i == 0:
                s_chan = le[n-1] - le[i]
                s_le = chan[n-1] - chan[i]
                dem += 1 if s_le == s_chan else 0
            else:
                s_chan = chan[i-1] + (le[n-1] - le[i])
                s_le = le[i-1] + (chan[n-1] - chan[i])
                dem += 1 if s_le == s_chan else 0
        return dem




sol = Solution()
nums = [2, 1, 6, 4]
print(sol.waysToMakeFair(nums))
