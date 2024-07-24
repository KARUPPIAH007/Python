# Cretaing a list:
# Creating same data type
course = ['Python' , 'Java' , 'Ruby'] #String
rollno = [123,345,567] #integer

# creating mixed data type/heterogeniuos
mixed_python = ['Karuppiah',123,True,67.88]
print('heterogenoius:' , mixed_python)
print('Length:' , len(mixed_python))
print('Access of karuppiah : ',mixed_python[0])
print('Access of 123 : ',mixed_python[1])
print('Access of True : ',mixed_python[2])
print('Access of 67.88 : ',mixed_python[3])
# NegativeIndex -> 123

# Slicing : [start:stop(excluded)]
print('Slicing :' , mixed_python[1:3])

print('Slicing :' , mixed_python[0:3])

# Negative slicing
print('Slicing :',mixed_python[-4:-2])

# Mutable (can change ,add, object)
fruits = ['Mango' , 'Banana', 'Graphs', 'WaterMelon']
fruits[1] = 'Kiwi'
print('Using Index Replacing banana with kiwi :' ,fruits)

del fruits[3]
print('Removing watermelon :', fruits)

fruits[1:3]=['apple','banana']
print(fruits)