def is_pali(arry):
    return arry==arry[::-1]

    

Arry=[]
n= int(input())

element = input()
element_list=list(map(int,element.split()))
Arry.extend(element_list)

result=is_pali(Arry)
if result:
    print("YES")
else:
    print("NO")