#PROGRAM TO DISPLAY FIBONACCI SERIES

terms=int(input("TILL HOW MANY TERMS?"))
#defining
num1,num2=0,1
temp=0

#conditions

if terms <= 0:
    print("please enter a positive interger!")
elif terms ==1:
    print("fibonacci series upto",terms,":")
    print(num1)
else:
    print("finoacci series :")
    while temp < terms:
        print(num1)
        nth_term = num1+num2
#updation
        num1=num2
        num2=nth_term
        temp += 1

