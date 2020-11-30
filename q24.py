def copy_list(list):
    copied = list.copy()
    return copied

list = [3,4,6,3]
clone = copy_list(list)

print(f"original list: id {id(list)} list {list}")
print(f"cloned list: id {id(clone)} list {clone}")