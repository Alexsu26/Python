n = float(input())
l, r = -10000, 10000
while r - l > 1e-8:
    mid = (l + r) / 2
    x = mid **3
    if x < n:
        l = mid
    else:
        r = mid
# print("%.6f" % (mid)) old
print("{:.6f}".format(mid))  # new