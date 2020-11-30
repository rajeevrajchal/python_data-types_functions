def remove_key(dict1, key):
    if key in dict1:
        dict1.pop(key)
    return dict1

print(remove_key({1: 1, 2: 4, 3: 9, 4: 16}, 2))