vowels = ['a', 'e', 'i', 'o', 'u']
def disemvowel(string):
    for vowel in vowels:
        string = string.replace(vowel, '')
        string = string.replace(vowel.upper(), '')
    return string
print(disemvowel("Hola como estas, espero que bien!"))