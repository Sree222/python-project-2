my_list=[]

n = int(input("enter number of elements:"))

for i in range(0,n):
    element=int(input())

    my_list.append(element)
print("your list:",my_list)

for i in my_list:
    if (i>=0):
        print("postive interger list:",i)
