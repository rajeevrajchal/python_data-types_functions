def concatenate_dic(dict1, dict2, dict3):
    dic={}
    for d in (dict1, dict2, dict3):
        dic.update(d)
    return dic


print(concatenate_dic({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60}))