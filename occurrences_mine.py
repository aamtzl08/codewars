def delete_nth(l,n):
    m = []
    for i in l:
        if m.count(i) < n: m.append(i)
    return m
