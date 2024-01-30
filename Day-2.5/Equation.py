def fun ( a , b):
    result = 0 
    power  = 0 
    for i in range(0 ,b+1,2):
        result+=(a**i)

    return result



a , b = map ( int , input().split())
ans = fun(a , b )
print( ans-1)
