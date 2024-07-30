# def sum(*args):
#     count = 0
#     for i in args:
#         count+= i
#     return count
# output = sum(1,2,3,4,5)
# print('Addition:',output)

# def func(*args):
#     for name in args:
#         print(name)
# def main():
#     Changepond = ["gokul","Karuppiah","Sravanan","Dhainsh",'Hamsa','vijay']
#     func(*Changepond)
# if __name__ == "__main__":
#     main() 

# def staffdetails(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} is {value}')
# def main():
#     changepond = {'Name':'Karuppiah',
#                   'Age':24,
#                   'MobileNo':9768657767
#                  }
#     staffdetails(**changepond)
# if __name__ =="__main__":
#     main()

# def make_sandwich(*items):
#     if not items:
#         print("You haven't added any items to your sandwich.")
#         return items

#     print("Sandwich Order:")
#     for item in items:
#         print(f"- {item}")
#     print("Your sandwich has been ordered with the above items.")

# def main():
#     # Define the tuple of items before calling make_sandwich
#     Make = ('lettuce', 'tomato', 'turkey', 'cheese', 'mayo')
#     make_sandwich(*Make)

# if __name__ == "__main__":
#     main()


# def print_list(*args):
#     for item in args:
#         print(item)

# def main():
#     size = int(input("Enter the number of items: "))
#     lst = [input("Enter an item: ") for _ in range(size)]
#     print("\n Original List:")
#     print_list(*lst)
#     index = int(input("\nEnter the index where you want to add new ingredients: "))
    
#     if index < 0 or index > len(lst):
#         print("Invalid index. No changes made.")
#         return
    
#     new_ingredients = input("Enter new ingredients (separated by commas): ").split(',')
    
#     for ingredient in(new_ingredients):
#         lst.insert(index, ingredient)
#     print("\nUpdated List:")
#     print_list(*lst)

# if __name__ == "__main__":
#     main()


def make_car(manufacturer,model,**kwargs):
    print(manufacturer)
    print(model)
    for key,value in kwargs.items():
        print(key,value)
def main():
    cars={} 
    manufacturer = input("enter manufacturer :")
    model = input("enter model : ")
    key='car'
    value=[ input("enter color: "),
           input('enter tow-package : ')
           ]
    cars[key]=value
    lst=[manufacturer,model]
    make_car(*lst,**cars)
 
if __name__=="__main__":
    main()

