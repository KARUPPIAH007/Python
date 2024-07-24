# create a tuple
# homogenoius
student_id = (123,124,125,126)
ice_cream = ('Butterscotch', 'Choco-chips','Blueberry')

# heterogenious
mixed_type = (123,'Hello' , False , 56.78)
# len()
# using index ==> bluberry(postive index)
# using slicing ==> 'Hello',False

print('Length:' , len(mixed_type))
print('Slicing :' , mixed_type[1:3])
print('Negative:' ,mixed_type[-2])
print(ice_cream.index('Blueberry'))
print(mixed_type.index(False))


ice_creame = ('Vanilla')        # str
print(ice_creame,type(ice_creame))
ice_creame = ('Vanilla',)       # comma (tuple)
print(ice_creame,type(ice_creame))

# immutable
#mixed_type[0] = True
#print("False ",mixed_type)


# count method
icecream=('vanilla','choco','blueberry','vanilla')
countmethod=icecream.count('vanilla')
print('count method;',countmethod)

# index method
indexmethod=icecream.index('vanilla')
print('indexmethod:',indexmethod)