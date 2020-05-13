def persistent(n):
    times = 0
    l = [i for i in str(n)]
    if len(l) <= 1:
        return times
    else:
        while len(l) > 1:
            times += 1
            num = 1
            for c in l:
                num *= int(c)
            l = [i for i in str(num)]
            print(l)
        return times
print(persistent(39))
