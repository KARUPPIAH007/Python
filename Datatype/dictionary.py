# Watch_details = {
#     'Titan':8000,
#     'Fastrack':5000,
#     'Omega':9000,
#     'Titan':12000
# }

# print('Watch_Available:',Watch_details)
# print('length of the dictionary:',len(Watch_details))
# print('Type:',type(Watch_details))
# print('Using Key',Watch_details['Titan'])



# Watch_details = {
#     'Titan':8000,
#     'Fastrack':5000,
#     'Omega':9000,
#     'Cartier':8000
# }
# print('Watch_Available:',Watch_details) # values can be repeated
# print('length of the dictionary:',len(Watch_details))
# print('Type:',type(Watch_details))
# print('Using Key',Watch_details['Titan'])
# print('Using Key',Watch_details['Cartier'])
# Watch_details['Omega']=4500
# print('After Modifying:',Watch_details)
# Watch_details['IWC']=5000
# print('Adding New Watch:',Watch_details)


#create a dictionary of fooditems and price(add,modify)

# food_item = {
#     'Chicken65':250,
#     'Mutton': 300,
#     'Fried Rice':260,
#     'Fish curry':390
# }

# print('Food Item and thier Prices',food_item)
# food_item['Mutton soup']=50
# print('Adding New Food:',food_item)
# food_item['Chicken65']=160
# print('After modifying',food_item)

#Nested Dictionary
users ={
    'KAR':{
        'firstname' : 'Karuppiah',
        'lastname' : 'saravanan',
        'Location' : 'KKDI'
    },
    'SAR':{
        'firstname' : 'saravanan',
        'lastname' : 'KARUPPIAH',
        'Location' : 'MDU'
    },
     'KD':{
        'firstname' : 'kaa',
        'lastname' : 'ssss',
        'Location' : 'MMM'
    },

}

for user_id, user_details in users.items():
    print(f"User ID: {user_id}")
    print(f"First Name: {user_details['firstname']}")
    print(f"Last Name: {user_details['lastname']}")
    print(f"Location: {user_details['Location']}")
    print()  



firstname = users['KAR']['firstname']
print(f"First name of KAR: {firstname}")

location= users['KD']['Location']
print(f"Location of KD: {location}")