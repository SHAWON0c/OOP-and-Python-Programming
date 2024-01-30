
def fun(n, digits):
    sum = 0 
    for digit in digits:
        sum+=int(digit)
    return sum
    


n = int(input())
digits = input()


result =fun(n, digits)
print(result)
