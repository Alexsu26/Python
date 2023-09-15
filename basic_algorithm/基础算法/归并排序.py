N = int(input())
seq = list(map(int, input().split()))


def merge_sort(my_list, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(my_list, left, mid)
    merge_sort(my_list, mid + 1, right)
    tmp = []
    i = left
    j = mid + 1
    while (i <= mid) and (j <= right):
        if my_list[i] <= my_list[j]:
            tmp.append(my_list[i])
            i += 1
        else:
            tmp.append(my_list[j])
            j += 1
    tmp += my_list[i : mid + 1]
    tmp += my_list[j : right + 1]
    my_list[left : right + 1] = tmp


merge_sort(seq, 0, N - 1)
print(' '.join(map(str, seq)))
