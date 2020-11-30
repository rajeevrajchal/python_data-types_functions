def not_poor(string):
    nott = string.find('not')
    poor = string.find('poor')
    if poor > nott and nott > 0 and poor > 0 :
        string = string.replace(string[nott: poor+4], 'good')
        
    return string

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
    