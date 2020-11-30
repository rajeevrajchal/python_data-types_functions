input1= input("Enter string1: ")
input2= input("Enter string2: ")

output1 = input2[:2] + input1[2:]
output2 = input1[:2] + input2[2:]

output = output1+" "+output2
print(output)