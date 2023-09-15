N = int(input())
seq = list(map(int, input().split()))

def quick_sort(my_list, left, right):
    if left >= right:
        return
    x =  my_list[(left + right) // 2]
    i = left - 1
    j = right + 1
    while i < j:
        while 1:
            i += 1
            if my_list[i] >= x:
                break
        while 1:
            j -= 1
            if my_list[j] <= x:
                break
        if i < j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
    quick_sort(my_list, left, j)
    quick_sort(my_list, j + 1, right)

quick_sort(seq, 0, N - 1)
print(' '.join(list(map(str, seq))))