p = [6, 3, 5, 7, 2]
d = [8, 4, 15, 20, 3]


def check(p, d):
    """
    thuật toán này gọi là More
    ý tưởng là ta sẽ chọn những thằng có thời hạn hoàn nhỏ nhất chọn trước
    nếu chọn thì xem nó có thỏa mãn là thêm thằng nhỏ đó vào liệu nó có đúng hạn hay ko
    nếu ko thì bỏ đi chọn thằng nhỏ nhất khác nhưng thỏa mãn đúng hạn
    => ý tưởng tham lam theo time hoàn thành công việc sort từ nhỏ đến lơn
    vd trong th của ta thì 5 có d nhỏ nhất chọn việc 5 , tiếp theo 2 có d nhỏ nhất chọn 2
    kiểm tra xem 5 rồi đến 2 thì thấy việc 5 xong làm việc 2 thì ko hoàn thành việc 2 -> loại 2 ko chon
    tiếp theo chọn vieecj nhỏ nhất còn lại là việc 1 với d = 8 thì thấy hoàn thành việc 5 rồi đến việc 1
    thì việc 1 cũng hoàn thành -> chọn 1 vậy js là [5,1]
    tiếp theo 5 -> 5,1 -> 5,1,3 -> 5,1,3,4

    """
    dict = {}
    s = 0
    for i in d:
        s += 1
        if i not in dict:
            dict[i] = s

    print(dict)
    s = 0
    js = []
    for i in range(len(d)):
        for j in range(len(d)):
            if d[j] >= d[i]:
                tmp = d[j]
                d[j] = d[i]
                d[i] = tmp

                tmp = p[j]
                p[j] = p[i]
                p[i] = tmp
    print(p)
    print(d)
    for i in range(len(d)):
        s += p[i]
        if s > d[i]:
            s -= p[i]
        else:
            js.append(i)
    print(js)
    js_tmp = []
    for i in js:
        js_tmp.append(dict[d[i]])
    print(js_tmp)
check(p, d)
