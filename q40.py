tuple = (1,2,3,4,5,6)
print(tuple)
tuple = tuple + (7,)
print(tuple)
tuple = tuple[0:5] + (23, ) + tuple[5:]
print(tuple)