def count_string(list):
    count = 0
    for word in list:
        if (word[0] == word[-1]):
            count+=1
    return count



print(count_string(['abc', 'xyzx', 'aba', '1221', 'sdfsdf']))