def unique_list(list1):
    list1 = set(list1)
    print(list1)
    list1 = list(list1)
    return list1

print(unique_list([3,4,4,4,4,5,6,7,6,6,4]))