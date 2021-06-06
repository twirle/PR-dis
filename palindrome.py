def palindrome(word):
    word = input("Enter word: ")
    if word[:] == word[::-1]:
        return True
    else:
        return False

print(palindrome(""))
