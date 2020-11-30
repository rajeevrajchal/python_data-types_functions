def exchange(input):
    output = input[-1] + input[1:-1] + input[0]
    return output

input = input("Enter the string: ")
output = exchange(input)
print(output)