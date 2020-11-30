def sort_tuple_last(tuples):
    return sorted(tuples, key= lambda n: n[-1])
  

print(sort_tuple_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
