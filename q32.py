def generate_dic(n):
    dict1 ={}
    for i in range(1,n+1):
        dict1.update({i: i*i})
    return dict1

print(generate_dic(4))
print(generate_dic(8))