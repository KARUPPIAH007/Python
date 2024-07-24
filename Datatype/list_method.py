menu_card = ['Panner' , 'Dal' ,'Rice']
print('Avaiable Items in MenuCard :',menu_card)
#append() --> adds on element at the end of the list
menu_card.append('Marai Kofta')
print('Add Kofta Items in MenuCard :',menu_card)
# Dal Tadka , Briyani
#extend() --> add the elements of the list to the end of the list(or iterable)
# to end list
menu_card.extend(['dal tadaka','biriyani'])
print("using extend method",menu_card)

# insert --> Adds an element at the specfied postion
menu_card.insert(1,'Mutton Briyani')
print("using insert method",menu_card)


# Remove() method -> It Will remove data
menu_card.remove('dal tadaka')
print("using remove method",menu_card)

# pop method -> removes element of  specified position
menu_card.pop(2)
print("using pop method",menu_card)

menu_card1= ['Panner' , 'Chicken' , 'Mutton']
# index Method
index_method = menu_card1.index('Chicken')
print('It will give position:',index_method)

Index_method = menu_card1.index('Panner')
print('It will give the position : ',Index_method) 

# sort method
menu_card1.sort()
print('sort position :',menu_card1)