#num = 1
# while num <=10 :
#     print( num)
#     num= num + 1 
#     if num ==5:
#         break

# while num <=10 :
#     if num ==5:
#         continue
#     print( num)
#     num= num + 1 

    

#for loop 


numbers = [ 1 , 2 , 3 , 4 , 5 ]
sum = 0 
for num in numbers:
        print(num)
        sum= sum + num

print(sum)

text = ' pagla hawa '
for char in text: 
        print( char)


#Range
    
range(1,10)
print( range)

for i in range(1, 10,2):
        print(i)

nums= [ 1 , 2, 3 , 4 , 5 , 6 , 7]
for i in nums:
        print(i , nums.index(i))