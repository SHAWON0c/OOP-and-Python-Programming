name = 'shawon siddikee'
name2 = " shawon siddikee "
name3 = """
    shawon siddike 
    the boss 


"""

name4 = 'shawon\'s siddikee' #escape 

print( name3)
print(name4)


#mutable means changeable 
#immutable means you cann't change it 

for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name[::-1])
print(name2[-3])

#change 

#name2[0]='R'
print(name2)

if 'siddikee' in name2:
    print('ache')

#boro/ chuto

print(name2.upper())