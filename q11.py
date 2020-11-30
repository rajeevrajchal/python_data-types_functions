def word_count(string):
    count = {}
    splitted = string.split()
    for word in splitted:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print(word_count("""I felt happy because I saw the others were happy and 
                because I knew I should feel happy but I wasn’t really happy"""))
