n, q = map(int,input().split())
arr = list(map(int, input().split()))
while q > 0:
    q -= 1
    x = int(input())
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > x:
            r = mid
        else:
            l = mid + 1
    if arr[l] != x:
        print("-1 -1")
        continue
    print(l, end = ' ')
    l, r = 0, n - 1
    while l < r:
        mid = (l + r + 1) >> 1
        if arr[mid] <= x:
            l = mid
        else:
            r = mid - 1
    print(l)