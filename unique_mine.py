def unique_in_order(iterable):
    l = []
    if len(iterable) > 0:
        l.append(iterable[0])
    
        for i in range(1, len(iterable)):
            if iterable[i - 1] != iterable[i]:
                l.append(iterable[i])
        return l
    return l

print(unique_in_order([]))