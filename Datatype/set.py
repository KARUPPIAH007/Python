# Creating a set

staff_id ={123,124,125,126} #same data type
mixed_type = {'Karuppiah',69,145,True}
print('Mixed Set:',mixed_type)
print('Length:',len(mixed_type))

s1 = {True,0,1,False}
print(s1)
# true -1
# false -0
s1 = {True,1}
print(s1)
s1 = {0,False}
print(s1)

for mixed in mixed_type:
    print(mixed)
more_add = {'Rahul',24}

#add()  method -> add element to the set
mixed_type.add('Gym akka')
print('Add method:', mixed_type)

# update() method
mixed_type.update(more_add)
print('Update method:',mixed_type)

# discard() -> remove specified element
mixed_type.discard(145)
print('Discard method:' ,mixed_type)

mixed_type.remove(24)
print('Remove method:',mixed_type)