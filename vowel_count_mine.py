def getCount(s):
    num_vowel = 0
    for i in 'aeiou':
        num_vowel += s.count(i)
    return num_vowel
print(getCount('Mi mama me mama'))
