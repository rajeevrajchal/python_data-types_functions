def check_empty(list):
    isEmpty = True
    for dic in list:
        if len(dic) != 0:
            isEmpty = False
    return isEmpty

print(check_empty([{}, {}]))
print(check_empty([{}, {'a': 23},  {}, {'b': 'fan'}]))