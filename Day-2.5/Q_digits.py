
def print_digits(n):

    reversed_digits = str(n)
    #print(reversed_digits[::-1])
    with_space=" ".join(reversed_digits[::-1])
    print(with_space)



t =int(input())
for _ in range(t):
    num = int(input())
    print_digits(num)