def add(list):
    sum= 0
    for num in list:
        sum+=num
    return sum

def multiply(list):
    mul = 1
    for num in list:
        mul *= num
    return mul

print(add([3,4,5,6,6,7]))
print(multiply([3,4,5,6,6,7]))