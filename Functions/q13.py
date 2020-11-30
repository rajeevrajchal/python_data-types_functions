def sort_tup_list(list_of_tuple):
    list_of_tuple.sort(key= lambda x: x[1])
    print(list_of_tuple)

list_of_tuple = [(3,4), (5, 6), (1,8), (3, 9)]
sort_tup_list(list_of_tuple)