def sort_dict_list(list_of_dict):
    list_of_dict.sort(key= lambda x: x['name'])
    print(list_of_dict)

list_of_dict = [{'name': "Ram"}, {'name': 'Sita'}, {'name': 'Hari'}, {'name': 'Gita'}]
sort_dict_list(list_of_dict)