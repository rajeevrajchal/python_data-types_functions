input = input("Enter the string: ")

if len(input)<3:
    output= input
else:
    if input[-3:]=="ing":
        output = input + "ly"
    else:
        output = input + "ing"

print(output)
