word="balaji srinivasan"
vowel="aeiou"
res=[char for char in word if char in vowel]
print(res)
print(word[::-1])
print(word[::-3])
print(word[::-2])
sep='-'.join(word[::2])
print(sep)
print(word[::-1])
print(word[::2])