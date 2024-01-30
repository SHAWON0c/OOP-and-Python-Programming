def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence


N = int(input())
if N==1:
    print(0)
else :
    result = fibonacci(N)
    print(*result)
