list1= [1,2,3,4,5,6,7,8]
print("Original element", list1)
print("Square of each element")
print(list(map(lambda x: x**2, list1)))
print("Cube of each element")
print(list(map(lambda x: x**3, list1)))