def merge_dic(dict1, dict2):
    dict1.update(dict2)
    return dict1

print(merge_dic({1: 1, 2: 4}, {10: 100, 11: 121, 12: 144}))