import os
import filecmp
def Comparefiles(filename1,filename2):
    if(not os.path.exists(filename1)):
        print("Not Exists:",filename1)
    elif(not os.path.exists(filename2)):
        print("Not Exists:",filename2)
    else:
        compare = filecmp.cmp(filename1,filename2)
        if compare ==True:
             print('Success-> The Files are Same')
        else:
            print('Failure -> The files are Different')
def main():
    file_01 = input('Enter the first filename:')
    file_02 = input('Enter the second filename:')
    Comparefiles(file_01,file_02)
if __name__ == "__main__":
    main()