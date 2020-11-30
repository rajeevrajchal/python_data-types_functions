input_string = input("Enter the input: ")

if len(input_string)<2:
    print("Empty String")
else:
    print(input_string[0:2]+input_string[-2:])
