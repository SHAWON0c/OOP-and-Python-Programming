
def swap (arry , a , b ):
    temp=arry[a]
    arry[a]=arry[b]
    arry[b]=temp 

Arry=[]
n = int ( input())

x = input()
x_list=list(map(int, x.split()))

Arry.extend(x_list)

mn_idx=Arry.index(min(Arry))
mx_idx=Arry.index(max(Arry))

swap(Arry,mn_idx , mx_idx)

for val in Arry:
    print(val , end=" ")





