country=['india','south korea','iran','japan','turkey','iraq']
for name in country:
    print(f"{name.title()}.These are the list of countries")

print()

author_name =('j k rowling','rachel aaron','veerna aardema')
for Name in author_name:
    print(f" {Name.title()}.These are the list of author")


# author_name =('j k rowling','rachel aaron','veerna aardema')
# print("The author_name is :")
# for name in author_name:
#     print(name.title())





for auth_name in range (len(author_name)):
    print(auth_name)

print()

for auth_name in range(len(author_name)):
    print(author_name[auth_name],'---',auth_name) 

#iterate a string using for loop
time_update="It's 4:15 pm"
for i in range(0,len(time_update)):
    print(time_update[i])