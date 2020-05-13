def isPrimer(n):
    return prime(n,2)

def prime(n,j):
    if(n<2):
        return False
    if(j==n):
        return True
    if(n%j==0):
        return False
    return prime(n,j+1)


# Driver Program
n = 1234
if (isPrimer(n)):
    print("Yes")
else:
    print("No")
