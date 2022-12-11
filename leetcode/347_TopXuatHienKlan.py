class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_tmp = {}
        for i in nums:
            if i not in dict_tmp:
                dict_tmp[i] = 1
            else:
                dict_tmp[i]+=1
        print(dict_tmp)
        my_keys = sorted(dict_tmp, key=dict_tmp.get, reverse=True)[:k]
        print(my_keys)
        return my_keys

sol = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
print(sol.topKFrequent(nums, k))
