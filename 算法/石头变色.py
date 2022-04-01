def rock_colour(rocks):
    n = len(rocks)
    if n % 2 != 0:
        return -1

    # 统计石头颜色总数
    zero = 0
    blue = 0
    red = 0
    cost = 0
    for i in range(0, n):
        colour = rocks[i][0]
        if colour == 0:
            zero += 1
            cost += rocks[i][1]
        elif colour == 1:
            red += 1
        else:
            blue += 1

    # 如果某颜色大于n/2则失败
    if red > n / 2 or blue > n / 2:
        return -1

    # 排序
    new_rocks = sorted(rocks, key=lambda r: (r[0], r[2] - r[1]), reverse=False)

    # 获取最小代价，cost+红变蓝色代价
    # 需要变蓝的个数
    blue = n // 2 - blue
    for i in range(0, blue):
        cost += new_rocks[i][2] - new_rocks[i][1]
    return cost


rocks = [
    [2, 1, 2],
    [2, 1, 2],
    [1, 1, 2],
    [0, 1, 9],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
]
print(rock_colour(rocks))
