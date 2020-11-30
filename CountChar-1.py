input_string = input("Enter the string: ")

result ={}
for i in input_string:
    result[i] = result.get(i, 0) +1

print(result)