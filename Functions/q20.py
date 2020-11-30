array1 = [1,2,3,4,5,6,7]
array2 = [6,7,9,10]

intersection = list(filter(lambda x: x in array1, array2))

print("intersection is: ", intersection)