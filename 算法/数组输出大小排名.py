def code2(arr):
    new_arr = sorted(set(arr))
    arr_dic = {}
    for idx, num in enumerate(new_arr):
        arr_dic[num] = (idx + 1)
    return [arr_dic[num] for num in arr]