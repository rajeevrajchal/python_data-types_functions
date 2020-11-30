def max_length(list):
    length =[]
    for word in list:
        length.append(len(word))
    return max(length)

wordlist = ['Helloooooooooooooo', 'fan', 'sun', 'fantastic'] 
longest = max_length(wordlist)
print(longest)