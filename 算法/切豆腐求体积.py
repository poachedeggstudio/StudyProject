def cutToufu(arr):
    n = len(arr)
    if n == 0 or arr is None:
        return HIGH * HIGH * HIGH
    # 数组排序
    arr = sorted(arr, key=lambda r: (r[0], r[1]))
    print(arr)
    i = 0
    l = 0
    r = HIGH
    while i < n and arr[i][0] == 1:
        new = arr[i][1]
        if new > l:
            if new < (r - l) // 2:
                l = new
            else:
                r = new
        i += 1
    max_x = r - l

    l = 0
    r = HIGH
    while i < n and arr[i][0] == 2:
        new = arr[i][1]
        if new > l:
            if new < (r - l) // 2:
                l = new
            else:
                r = new
        i += 1
    max_y = r - l

    l = 0
    r = HIGH
    while i < n and arr[i][0] == 3:
        new = arr[i][1]
        if new > l:
            if new < (r - l) // 2:
                l = new
            else:
                r = new
        i += 1
    max_z = r - l

    print(max_x, max_y, max_z)
    return max_x * max_y * max_z


HIGH = 100
a = [(1, 1), (1, 10), (2, 99), (3, 80), (3, 5), (2, 40), (1, 9)]
print(cutToufu(a))
