class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        # nếu tất cả đều bằng 5 5 5 thì max = 1
        max = 1
        start = 0
        end = 0
        s = 0
        while start + 1 < n:

            if arr[start] == arr[start + 1]:
                start += 1
                continue
            end = start + 1
            while end + 1 < n and ((arr[end] > arr[end - 1] and arr[end] > arr[end + 1]) or (
                    arr[end] < arr[end - 1] and arr[end] < arr[end + 1])):
                end += 1
            s = end - start + 1
            if max < s:
                max = s
            start = end
        return max


nums = [9, 4, 2, 10, 7, 8, 8, 1, 9]
# nums = [4,8,12,16]
sol = Solution()
print(sol.maxTurbulenceSize(nums))
