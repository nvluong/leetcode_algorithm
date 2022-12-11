class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = 1
        r = len(arr)-2


        while l <= r:
            mid = int((l+r)/2)
            if (arr[mid-1] < arr[mid]) and (arr[mid+1] < arr[mid]):
                return mid

            elif (arr[mid-1] > arr[mid]) and (arr[mid+1] < arr[mid]):
                r = mid-1
            else:
                l = mid+1


sol = Solution()
arr = [1,10,15,2]
print(sol.peakIndexInMountainArray(arr))