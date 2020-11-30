is_digit = lambda x: x.replace('.', '').isdigit()

print(is_digit('34'))
print(is_digit('3.4'))
print(is_digit('1a'))
print(is_digit('a1'))