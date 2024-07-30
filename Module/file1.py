#open() function -> filename,mode(r,w,a,...)

# file_read = open('C:/Users/karuppiah.c/Desktop/Python/Module/calculate.py','r')
# print(file_read.read())

import os

def CreateFile(filename): #filename = calculate.py
 #filename = fileread.py
    if(os.path.exists("Module/"+filename)):#True #False
        print('File is already exists')
    else:
        file_create = open("Module/"+filename,'w')

def main():
    print("Enter the filename  you want to create:")
    file_name = input()

    CreateFile(file_name)

if __name__ == "__main__":
    main()