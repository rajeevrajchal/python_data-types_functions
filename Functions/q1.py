def max_of_3(a, b, c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
    
print(max_of_3(4,2,6))