def unique_word(string):
    words = string.split(',')
    words = set(words)
    return(sorted(words))

input = input("Enter the comma separated sequence of words: \n")
print(unique_word(input))