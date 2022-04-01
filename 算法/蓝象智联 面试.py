# 格式化文件大小
# 输入：文件大小（Bytes），int类型
# 输出：人性化显示文件大小。
# 例子：
#   56 -> 56B
#   56215 -> 54.9KB
#   26353560 -> 25.1MB
#   12312312312 -> 11.5GB

def code1(num, key=1):
    l = ['B', 'KB', 'MB', 'GB']
    n = num // (1024 ** key)
    if n == 0:
        if key == 0:
            return f'{num}B'
        else:
            n = num / (1024 ** key)
            return '%0.1f%s' % (n, l[key - 1])
    key += 1
    return code1(num, key)


# # 写一个函数找出一个整数数组中，第二大的数
def code2(arr):
    return sorted(arr)[-2]


# 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# - 左括号必须用相同类型的右括号闭合。
# - 左括号必须以正确的顺序闭合。
# 示例：
# "()" -> true
# "()[]{}" -> true
# "(]" -> false
# "[()]{}" -> true

def code3(string):
    n = len(string)
    if n < 2:
        return False
    a = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    new_string = [string[0]]
    for i in range(1, n):
        if len(new_string) == 0:
            new_string.append(string[i])
            continue
        if a[new_string[-1]] == string[i]:
            new_string.pop()
        else:
            new_string.append(string[i])
    if len(new_string) == 0:
        return True
    else:
        return False


