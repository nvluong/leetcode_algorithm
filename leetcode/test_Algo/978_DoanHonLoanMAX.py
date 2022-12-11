def check(arr, end):
    return ((arr[end] > arr[end+1] and arr[end] > arr[end-1]) or
                      (arr[end] < arr[end+1] and arr[end] < arr[end-1]))
def max_HonLoan(nums):
    """
        b1 : khởi tạo start, end = 0, max = 1
        b2 : lặp cho start chạy từ 0 đến n-1
        b3 : nếu mà gặp 2 thằng bằng nhau thì start tăng lên 1 và bỏ ko thực hiện gì khi đó tức dùng continue
        b4 : end = start + 1
            // tại vì sao lại start + 1 vì chúng ta muốn kiếm tra cả i-1, i, i+1 thấy i+1 cuối tức là end = i+1
        b5 : kiểm tra nếu end mà chưa phải phần tử cuối và tại end thỏa mãn hỗn loạn
            thì ta lặp để tăng end lên 1 đơn vị cho đến khi hết hỗn loạn
        b6 : nếu vòng lặp tăng end kết thúc thì ta cập nhật start = end để tiếp tục
        b7 : tính lenght và so sánh với max
        :param nums:
        :return:
        """

    n = len(nums)
    print("n ", n)
    start = 0
    end = 0
    max = 1
    for i in range(len(nums) - 1):
        if nums[start] == nums[start+1]:
            start = i+1
            continue
        end = start + 1
        print("edn dau ", end)
        print("start ", start)
        while end < n-1 and check(nums, end):
            print("end1 ", end)
            end +=1
            print("end ", end)

        length = end - start + 1
        if max < length:
            max = length
        start = end

    return max

#       0  1  2  3   4  5  6  7  8
nums = [9, 4, 2, 10, 7, 8, 8, 8, 9]
# nums = [4,8,12,16]
print(max_HonLoan(nums))