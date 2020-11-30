def add(list):
    sum = 0
    for num in list:
        sum += num
    return sum

def multiply(list):
    mul = 1
    for num in list:
        mul *=num
    return mul

def max_num(list):
    return max(list)

def min_num(list):
    return min(list)


list = []
n = int(input("How many items: "))
print("Enter the numbers in list")
for _ in range(n):
    a = int(input())
    list.append(a)
    
print(add(list))
print(multiply(list))
print(max_num(list))
print(min_num(list))
