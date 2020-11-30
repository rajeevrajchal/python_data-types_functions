def insert_begin(list, string):
    new_list = []
    for word in list:
        word = string + str(word)
        new_list.append(word)
    return new_list

print(insert_begin([1,2,3,4], 'emp'))