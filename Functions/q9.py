def prime(n):
    if n==1:
        return False
    else:
        for i in range(2, n):
            if(n%i==0):
                return False
        return True

print(prime(2))
print(prime(1))
print(prime(7))
print(prime(8))
print(prime(9))