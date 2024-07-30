# write a program which will check the number is greater and equal to 
# 70 less than and equal to 90


def  check_Number(Number):
    if(Number>=70 and Number<=90):
        return Number
def main():
    size = int(input('Enter the size:'))
    lst = []
    print('Enter the values:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User list:',lst)

    filter_list = list(filter(check_Number,lst))
    print('Filter value:',filter_list)
if __name__ == "__main__":
    main()