def check_key(dict1, key):
    keys = dict1.keys()
    if key in keys:
        return "key exists"
    return "key doesnot exists"

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(check_key(dic, 2))
print(check_key(dic, 7))