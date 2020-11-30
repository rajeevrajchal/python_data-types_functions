numbers = [1, 4, 2, 5, 7, 3, 7, 9]
print("Original list: ", numbers)

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even elements in list", even)

odd = list(filter(lambda x: x % 2 != 0, numbers))
print("Even elements in list", odd)
