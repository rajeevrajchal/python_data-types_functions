def unpack_tuple(tup):
    n1, n2, n3 = tup
    print(n1, n2, n3)

def unpack_tuples(tup):
    n1, *n2, n3 = tup
    print(n1, n2, n3)


unpack_tuple((2,3,4))
unpack_tuples((2,3,4, 5, 6, 7))

