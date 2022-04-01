def code1(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return code1(n - 1) + code1(n - 2)


def code2(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    x = 1
    y = 2
    r = 0
    while n >= 3:
        r = x + y
        x = y
        y = r
        n -= 1
    return r