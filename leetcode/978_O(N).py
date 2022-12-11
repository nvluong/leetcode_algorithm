

def maxTurbulenceSize(arr):
    """
    cách sử dụng 1 vòng for O(N), chia làm 3 th, ==, > , <
    b1 : duyệt for i từ 0 đên len(arr)
    b2 : nếu arr[i] == ar[i+1] thì length = 2 và continue, tại sao length = 2 vì
        vd đoạn 7 8 8 hoặc 9 8 8 thì   đều có length là 78 hoặc 98 = 2
    b3 : nếu mà arr[i] < arr[i+1] ta sử dụng biến flag để cắm cờ thể hiện độ lật của dấu > or <
         nếu arr[i] < arr[i+1] mà sử dụng flag = True thì khi phần
         arr[i] > arr[i+1] phải sử dụng flag = False
         vì nếu thỏa mãn là 1 điểm  hỗn loạn thì dấu phải luân phiên nhau
         tức flag phải luân phiên thay đổi tù True -> False và False -> True
    b4 : nếu arr[i] > arr[i+1] thì flag = đối nghịch với bên trên
    b5 : tính length rồi so sánh vs max
    :param nums:
    :return:
    """
    max = 1
    s = 1
    flag = True
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            s = 1
            continue
        if arr[i] < arr[i+1]:
            if flag == True:
                s+=1
            else: s= 2
            flag = False
        if arr[i] > arr[i+1]:
            if flag == False:
                s+=1
            else: s= 2
            flag = True
        if max < s:
            max = s
    return max
#       0 1 2 3 4 5 6 7
nums = [9,4,2,10,7,8,8,1,9]
print(maxTurbulenceSize(nums))