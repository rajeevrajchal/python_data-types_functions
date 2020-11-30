input_string = input("Enter the input: ")

first = input_string[0]
output= input_string[1:].replace(first, '$')

print(first+output)