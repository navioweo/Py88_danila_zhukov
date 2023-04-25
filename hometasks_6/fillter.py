words = ('level', 'racecar', 'python', 'madam', 'civic', 'hello')


def is_palindrome(word):
    return word == word[::-1]


palindromes = tuple(filter(lambda word: is_palindrome(word), words))
print(palindromes)
