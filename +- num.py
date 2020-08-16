my_list=[]

n = int(input("enter number of elements:"))

for i in range(0,n):
    element=int(input())

    my_list.append(element)
print("your list:",my_list)

for i in my_list:
    if (i<=0):
        my_list.remove(i)
i+=1
print("positive interger list:",my_list)
