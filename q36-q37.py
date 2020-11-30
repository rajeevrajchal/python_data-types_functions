def add_items(dict1):
    sum = 0
    for value in dict1.values():
        sum += value
    return sum

def multiply_items(dict1):
    mul =1
    for value in dict1.values():
        mul *= value
    return mul


print(add_items({10: 100, 11: 121, 12: 144}))
print(multiply_items({1: 1, 2: 4, 3: 9, 4: 16}))
