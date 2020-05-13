def getCount(s):
    return sum(c in 'aeiou' for c in s)

print(getCount('Mi mama me mama'))