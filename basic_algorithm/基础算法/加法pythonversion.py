if __name__ == '__main__':
    a = list(map(int, input()))[::-1]
    b = list(map(int, input()))[::-1]

    C = []
    t = 0
    i = 0
    while i < max(len(a), len(b)) or t :
        if i < len(a):
            t += a[i]
        if i < len(b):
            t += b[i]
        C.append(t % 10)
        t //= 10
        i += 1
    
    print(''.join(map(str, C[::-1])))
