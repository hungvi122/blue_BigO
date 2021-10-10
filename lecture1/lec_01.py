def night_museum():
    s = input()
    count = 0
    start = 'a'
    for i in s:
        step = abs(ord(i) - ord(start))
        start = i
        count += step if step <= 13 else 26 - step
    print(count)


def bear_game():
    n = input()
    arr = input().split()
    time_watch = 0
    for i in arr:
        if int(i) - 15 > time_watch:
            break
        else:
            time_watch = int(i)
    time_watch += 15
    time_watch = 90 if time_watch > 90 else time_watch
    print(time_watch)


def vitaly_str():
    s = input()
    t = input()
    result = ''
    size = len(s)
    plus = 1
    for i in s[-1:-len(s)-1:-1]:
        next_step = ord(i) + plus - ord('a')
        plus = next_step // 26
        result = chr(next_step % 26 + ord('a')) + result
        
    if result != t:
        print(result)
    else:
        print("No such string")


def check_array():
    na_nb = input()
    k,m = [int(i) for i in input().split()]

    str_arr_a = input().split()
    str_arr_b = input().split()

    max_k_a = int(str_arr_a[k-1])
    min_m_b = int(str_arr_b[len(str_arr_b) - m])

    if max_k_a >= min_m_b:
        print("NO")
    else:
        print("YES")


def big_segment():
    n = int(input())
    lst_segment = []
    min_arr, max_arr = -1, -1
    for i in range(n):
        segment = input().split()
        s = int(segment[0])
        e = int(segment[1])
        min_arr = s if (min_arr == -1 or min_arr > s) else min_arr
        max_arr = e if (max_arr == -1 or max_arr < e) else max_arr
        tb_segment = (s, e)
        lst_segment.append(tb_segment)
    index = -1
    if (min_arr, max_arr) in lst_segment:
        index = lst_segment.index((min_arr, max_arr)) + 1
    print(index)


def check_pass():
    n,k = [int(i) for i in input().split()]

    map_pass = {}
    for i in range(n):
        item = input()
        count = map_pass.get(len(item), 0)
        map_pass[len(item)] = count + 1
    pass_correct = input()
    count_min_pass, count_max_pass = 0, 0
    for key, value in map_pass.items():
        if key < len(pass_correct):
            count_min_pass += value

    count_max_pass = count_min_pass + map_pass.get(len(pass_correct))

    min_check = count_min_pass + count_min_pass//k * 5 + 1
    max_check = count_max_pass + (count_max_pass-1)//k * 5
    print(min_check, max_check)


def suffix_struct():
    s = input()
    t = input()
    s_sort = sorted(s)
    t_sort = sorted(t)

    if len(s) < len(t):
        return "need tree"
    elif len(s) == len(t):
        if s_sort == t_sort:
            return "array"
        else:
            return "need tree"

    # automaton check
    si, ti = 0, 0
    while si < len(s) and ti < len(t):
        if t[ti] == s[si]:
            ti += 1
            si += 1
        else:
            si += 1
    if ti == len(t):
        return "automaton"

    # check both or need tree
    for i in t:
        if t.count(i) > s.count(i):
            return "need tree"
    return "both"



