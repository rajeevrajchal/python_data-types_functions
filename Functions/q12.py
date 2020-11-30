def mul_unknown(n):
    return lambda x: x*n

output = mul_unknown(5)
print(output(4))    