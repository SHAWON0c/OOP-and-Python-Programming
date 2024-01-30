def fun( a, b):
    if a>b:
        a , b = b , a 
    total_sum=0
    for num in range(a+1,b):
        if num%2==1:
            total_sum+=num
    return total_sum


t = int( input())

for _ in range(t):
    a , b = map( int , input().split())
    ans = fun(a, b)
    print( ans )