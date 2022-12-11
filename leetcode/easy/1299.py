class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp = arr[:]
        for i in range(len(arr)-1):
            temp[i] = max(arr[i+1:])
        temp[len(arr)-1] = -1
        return temp

sol = Solution()
arr = [17,18,5,4,6,1]
print(sol.replaceElements(arr))
