def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
print(disemvowel("Hola como estas, espero que bien"))