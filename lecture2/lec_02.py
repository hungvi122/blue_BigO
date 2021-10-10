def wrath():
    n = int(input())
    arr = [int(str_val) for str_val in input().split()]

    arr_check = [1] * n
    for i in range(n-1, -1, -1):
        ls = i-arr[i] if i - arr[i] >= 0 else 0
        arr_check[ls:i] = [0] * (i - ls)
    return arr_check.count(1)


def chocolate():
    n = int(input())
    arr = [int(str_val) for str_val in input().split()]

    a_i, b_i = -1, n
    a_time, b_time = 0, 0
    while b_i - a_i > 1:
        if a_time == b_time:
            a_i += 1
            a_time += arr[a_i]
            if b_i - a_i > 1:
                b_i -= 1
                b_time += arr[b_i]
            else:
                break
        elif a_time < b_time:
            a_i += 1
            a_time += arr[a_i]
        else:
            b_i -= 1
            b_time += arr[b_i]
    return a_i + 1, n - a_i - 1


def play_card():
    n = int(input())
    arr = [int(str_val) for str_val in input().split()]
    a_point, b_point = 0, 0
    i, j = 0, n - 1
    while i <= j:
        # Turn B
        if arr[i] >= arr[j]:
            a_point += arr[i]
            i += 1
        else:
            a_point += arr[j]
            j -= 1

        if i > j:
            break

        # Turn B
        if arr[i] >= arr[j]:
            b_point += arr[i]
            i += 1
        else:
            b_point += arr[j]
            j -= 1

    return a_point, b_point


def get_index_array():
    n,k = [int(i) for i in input().split()]

    arr = [int(str_val) for str_val in input().split()]
    map_checkdup_right = {}
    index_right = 0
    while index_right < n:
        map_checkdup_right[arr[index_right]] = 1
        if len(map_checkdup_right) == k:
            break
        index_right += 1
    if index_right == n:  # not found
        return -1, -1

    map_checkdup_left = {}
    index_left = index_right
    while index_left > 0:
        map_checkdup_left[arr[index_left]] = 1
        if len(map_checkdup_left) == k:
            break
        index_left -= 1

    return index_left + 1, index_right + 1


def george_and_round():
    n,k = [int(i) for i in input().split()]

    arr_require = [int(str_val) for str_val in input().split()]
    arr_prepare = [int(str_val) for str_val in input().split()]

    i,j = 0, 0
    count = 0
    while i < n and j < k:
        if arr_require[i] <= arr_prepare[j]:
            i += 1
            j += 1
            count += 1
        else:
            j += 1

    return n - count


def read_book():
    n, time = [int(i) for i in input().split()]
    arr_book = [int(str_val) for str_val in input().split()]

    start, current, count_book = 0,0,0
    while current < n:
        if time - arr_book[current] >= 0:
            time -= arr_book[current]
            current += 1
        elif start == current:
            start, current = current + 1, current + 1
        else:
            count_book = count_book if count_book >= current - start else current - start
            time += arr_book[start]
            start += 1

    count_book = count_book if count_book >= current - start else current - start
    return count_book


def dress_vests():
    n,m,x,y = [int(i) for i in input().split()]

    arr_dress_required = [int(str_val) for str_val in input().split()]
    arr_dress_available = [int(str_val) for str_val in input().split()]

    i, j = 0, 0
    count = 0
    pair_index = []
    while i < n and j < m:
        if (arr_dress_required[i] + y) >= arr_dress_available[j] >= arr_dress_required[i] - x:
            count += 1
            pair_index.append((i + 1, j + 1))
            i += 1
            j += 1
        elif arr_dress_required[i] > arr_dress_available[j]:
            j += 1
        else:
            i += 1

    return count, pair_index


def approximate():
    n = int(input())
    arr = [int(str_val) for str_val in input().split()]

    max_val, min_val = arr[0], arr[0]
    i_max, i_min = 0, 0
    i_start, i_current = 0, 1
    max_range = 0
    while i_current < n:
        # update max, min
        if arr[i_current] >= max_val:
            max_val = arr[i_current]
            i_max = i_current
        if arr[i_current] <= min_val:
            min_val = arr[i_current]
            i_min = i_current

        # check max - min == 1
        if max_val - min_val > 1:
            max_range = max_range if i_current - i_start < max_range else i_current - i_start
            # update gia tri
            i_start, i_min, i_max = (i_max + 1, i_min, i_max + 1) if i_min > i_max else (i_min + 1, i_min + 1, i_max)
            # update gia tri min, max
            max_val = arr[i_max]
            min_val = arr[i_min]
        # increase index
        i_current += 1

    max_range = max_range if i_current - i_start < max_range else i_current - i_start
    return max_range


