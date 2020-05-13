def persistent(n):
    times = 0
    l = str(n)
    if len(l) <= 1:
        return times
    else:
        while len(l) > 1:
            num = 1
            for c in l:
                num *= int(c)
            l = str(num)
            times += 1
        return times

print(persistent(11))
