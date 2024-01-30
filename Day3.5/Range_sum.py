
def sub_sum(p,a, b):
    return p_sum[b]-p_sum[a-1]


def prefix_sum(arry):
    pre_sum=[0]
    cur_sum=0
    for num in arry:
        cur_sum+=num
        pre_sum.append(cur_sum)
    return pre_sum

Arry = []
n, q = map(int, input().split())

ele = input()
ele_list = list(map(int, ele.split()))
Arry.extend(ele_list)

p_sum = prefix_sum(Arry)
for _ in range (q):
    a , b = map(int, input().split())
    result= sub_sum(p_sum,a , b)
    print(result)