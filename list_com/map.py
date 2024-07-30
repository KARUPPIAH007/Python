# from functools import reduce
# def main():
#     size=int(input('Enter the size:'))
#     lst=[]
#     print("Enter the values:")
#     for i in range(size):
#         value=int(input())
#         lst.append(value)
#     print('User List :',lst)

#     map_list=list(map(lambda X: X**3,lst))
#     print("map list is :",map_list)
#     print()

#     reduce_list = reduce((lambda num1,num2:num1+num2),map_list)
#     print("Reduce value:",reduce_list)
# if __name__=='__main__':
#     main()   


# course = ['', 'python', '', 'Angul;ar', '']
# filtered_course = list(filter(lambda x,: x != '', course))
# print(filtered_course)


# def filtering(x,chars):


#     for i in chars:
#         if i in x:
#             return False
   
#     return True
# def main():
 
#     chars=[",",';']
#     course=['','python','java',',,','angul;ar','php']
#     print(list(filter(lambda x : filtering(x,chars) and x!='',course)))
 
# if __name__ == "__main__":
#     main()

# def main():
#     product_id = ['HEM-234', 'HEM-123', 'HEM-566']
#     output = [int(item.split('-')[1]) for item in product_id]
#     print(output)

# if __name__ == "__main__":
#     main()

detail=[
{'name':'shreya','age':15},
{'name':'pratiksha','age':13},
{'name':'prerna','age':15}
 
]
sorted_list = sorted( detail, key=lambda val: val['age'] )
print(sorted_list)


