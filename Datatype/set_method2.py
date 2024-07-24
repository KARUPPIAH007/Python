company = {'Infosys','ICIC Bank','TCS','Bajaj'}
add_company = {'SBI','Tata consultancy','Infosys','TCS'}

unoin_method = company.union(add_company)
print('Unoin Method will return all the element:' , unoin_method)

print()

unoin_method = company | add_company
print('Using Opertaor:', unoin_method)
print()

intersection_method = company.intersection(add_company) # opertor &
print('Instersection method will be return common elements:',intersection_method)
print()

#difference method -> returns the different element presented in the two sets
difference_method = company.difference(add_company)
print('difference Method:',difference_method)


difference_method =add_company.difference(company)
print('difference Method:',difference_method)