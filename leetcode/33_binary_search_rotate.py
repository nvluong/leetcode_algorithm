def binary_search_Rotate(nums, val):
    # b1 : khai bao 2 con tro
    l = 0
    r = len(nums) - 1
    # b2: lap l <= r:
    while (l <= r):
        # tại sao vẫn là l <= r bởi vì dù nó là 1 phần của mảng giảm thì l sẽ là r và r sẽ là l và ngược lại
        # b3: khởi tạo pivot
        mid = int((r + l) / 2)
        if val == nums[mid]:
            return mid
        elif nums[l] <= nums[mid]:
            if val >= nums[l] and val < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if val <= nums[r] and val > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

nums = [4,5,6,7,0,1,2,3,4]
val = 3
print(binary_search_Rotate(nums, val))
