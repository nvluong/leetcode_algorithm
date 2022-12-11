class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Cach 1: O(n*m)
        # nums.sort()
        # print(nums)
        # res = []
        # for i in queries:
        #     s = 0
        #     dem = 0
        #     for j in nums:
        #         s+=j
        #         dem+=1
        #         if s > i:
        #             dem-=1
        #             break
        #     res.append(dem)
        # return res

        # Cach 2: O(n)
        nums.sort()
        prefix = []
        s = 0
        for i in nums:
            s += i
            prefix.append(s)

        for i, n in enumerate(queries):
            queries[i] = (n, i)

        queries = sorted(queries, key=lambda x: x[0])
        print(queries)

        i = 0
        j = 0
        res = [0] * len(queries)
        while i < len(nums) and j < len(queries):
            if queries[j][0] < prefix[i]:
                res[queries[j][1]] = i
                j += 1
            else:
                i += 1
        print("i ", i)
        while j < len(queries):
            res[queries[j][1]] = i
            j += 1
        return res


sol = Solution()

nums = [4,2,3,5,1]
queries = [3,10,21]
print(sol.answerQueries(nums, queries))