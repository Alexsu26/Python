a = list(map(int, input()))
b = list(map(int, input()))


def my_add(A, B):
    C = []
    t = 0
    for i in range(0, max(len(A), len(B))):
        if i < len(A):
            t += A[i]
        if i < len(B):
            t += B[i]
        C.append(t % 10)
        t //= 10
    if t > 0:
        C.append(1)
    return C
if __name__ == '__main__':
    A = []
    B = []
    for i in range(len(a)-1, -1, -1):
        A.append(int(a[i]))
    for i in range(len(b)-1, -1, -1):
        B.append(int(b[i]))

    C = my_add(A, B)
    print(''.join(map(str,C[::-1])))
