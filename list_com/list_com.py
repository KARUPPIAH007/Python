# using list comphresion creating a list of square numbers

# new_list = [expression for number in iterable]

# new_list = [expression for number in iterable if(optional)]

new_list = [i for i in range(1,12)]
print('List comphresion:', new_list)


new_list = [i for i in range(1,12) if(i%2==0)]
print('List comphresion:',new_list)

vowels = ['a','e','i','o','u']
name="karuppiah"
without_vowels = [i for i in name if i  in vowels]
print(without_vowels)


vowels = ['a','e','i','o','u']
name="karuppiah"
without_vowels = [i for i in name if i  not in vowels]
print(without_vowels)