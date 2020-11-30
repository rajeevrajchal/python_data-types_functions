def removechar(word, n):
    new_word=''
    for i, char in enumerate(word):
        if i == n:
            continue
        else:
            new_word+=char
    return new_word


word = input("Enter the word: ")
if word:
    index = int(input("Enter which index char do you want to remove: "))

print("Before removing ", word)
word = removechar(word, index)
print(word)
