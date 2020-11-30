tup = (3,4,6,7, 2,3)
print(tup)
tup = tup[:3]+ tup[4:]
print(tup)

tup = list(tup)
tup.remove(4)
tup = tuple(tup)
print(tup)