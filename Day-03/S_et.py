#set unique items 

#list-> []
#tuple-> ()
# set-> {}
#set unique : no duplicate 


numbers =[12,23,23, 12, 15, 17, 23]
#numbers.add(20)
print( numbers)


numbers_set = set(numbers)
numbers_set.remove(12)
print(numbers_set)