def count_upper_lower(string):
    upper = 0
    lower =0
    for char in string:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
        else:
            pass
    print("No. of Upper case characters: ", upper)
    print("No. of Lower case characters: ", lower)


count_upper_lower('The quick Brow Fox')

