import math

blockSlots = [
    {
        'id': 1,
        'startTime': 0,
        'endTime': 20
    },
    {
        'id': 2,
        'startTime': 40,
        'endTime': 100
    },
    {
        'id': 3,
        'startTime': 110,
        'endTime': 150
    },
    {
        'id': 4,
        'startTime': 160,
        'endTime': 180
    },
    {
        'id': 5,
        'startTime': 190,
        'endTime': 200
    }
]

n = 10
def check(blockSlots, n):
    dict_tmp = {}
    for i in range(len(blockSlots)):
        dict_tmp[blockSlots[i]['startTime']] = blockSlots[i]['endTime']
    a = dict(sorted(dict_tmp.items()))
    max = 0
    for k, v in a.items():
        if k > max:
            lech = k - max
            if lech == n:
                return {'startTime': max, 'endTime': k}
            elif lech > n:
                return {'startTime': max, 'endTime': max + n}
        if v > max:
            max = v
    lech1 = 1440 - max
    if lech1 > n:
        return {'startTime': max, 'endTime': max + n}
    if lech1 - n < 0:
        return 'Cant find any non-blocking slot'

print(check(blockSlots, n))
