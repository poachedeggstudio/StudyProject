def minCandy(arr):
    n = len(arr)
    if arr is None or n == 0:
        return 0
    if n == 1:
        return 1
    l_candy = [1]
    r_candy = [1]
    # 左右坡度
    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            l_candy.append(l_candy[i - 1] + 1)
        else:
            l_candy.append(1)

        if arr[n - i] < arr[n - i - 1]:
            r_candy.insert(0, r_candy[0] + 1)
        else:
            r_candy.insert(0, 1)
    print(l_candy)
    print(r_candy)

    # 最小糖果数
    candy = 0
    for i in range(0, n):
        candy += max(l_candy[i], r_candy[i])
    return candy


def ringMinCandy(arr):
    n = len(arr)
    if arr is None or n == 0:
        return 0
    if n == 1:
        return 1
    # 寻找局部洼地
    low = 0
    if n == 2:
        low = arr.index(min(arr[0], arr[1]))
    else:
        for i in range(0, n):
            if arr[i - 1] >= arr[i] and arr[i] <= arr[i + 1]:
                low = i
                break
    arr = arr[low:] + arr[0:low] + [arr[low]]
    print(arr)
    return minCandy(arr) - 1


# print(minCandy([3, 1, 4, 3, 2, 5, 5, 6]))
print(ringMinCandy([3,3,3,3,3]))
