Watch_details = {
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Titan':12000
}

#keys() -> return a list containing the dictionary's keys
key_method = Watch_details.keys()
print('Key method:' , key_method)


value_method = Watch_details.values()
print('Value method:' , value_method)

# get method => returns the value of specified key
get_method = Watch_details.get('Titan')
print('get method:',get_method)


# items() method
item_method = Watch_details.items()
print('item method :',item_method)

# update method
Watch_details.update({'Noise':12000})
print('Update method:',Watch_details)

Watch_details.pop('Titan')
print('Pop method:',Watch_details)