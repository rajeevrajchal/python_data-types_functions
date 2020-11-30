def remove_odd_index(input):
    out_string =''
    for i in range(len(input)):
        if i%2 ==0:
            out_string +=input[i]
    return out_string

print(remove_odd_index("Hello"))
print(remove_odd_index("fantastic"))