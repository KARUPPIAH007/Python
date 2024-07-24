# #dynamic input
def count_num(lst,number):
   count =0
   for i in lst:
      if(i==number):
        count +=1
   return count

def main():
    print('Enter size of the  list')
    size = int(input())
    data_input = []
    print('Enter the value:')
    for i in range(size): #4
        value = int(input())
        data_input.append(value)
    print('User List:',data_input)

    SearchNum =int(input('Enter element to be checked list:'))
    print(SearchNum, " is repeating :",count_num(data_input,SearchNum)),""
main()

# num = int(input('Enter the Number:'))
# if(num%2==0):
#     print(f'{num} is even')
# else:
#     print(f'{num} is not even')
# print()

    