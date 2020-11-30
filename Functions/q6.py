def inRange(low, high, num):
    if num > low and num < high:
        return True
    else:
        return False

print(inRange(4, 8, 5))
print(inRange(4, 8, 10))