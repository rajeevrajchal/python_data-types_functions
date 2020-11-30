def insert_string_middle(str1, str2):
    str = ''
    mid = len(str1)//2
    str = str1[0:mid] + str2 + str1[mid:]
    return str

print(insert_string_middle('[[]]<<>>', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))