def addition(x,y):
    return x + y
def substraction(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y
def percentage(x,y):
    return (x/y)*100

print("enter operation to be performed")
print("1.addition")
print("2.substraction")
print("3.division")
print("4.multiplication")
pr
choose_operation=input("enter the choice ")
number_1=int(input("enter the first number"))
number_2=int(input("enter the second number"))
if choose_operation=='1':
    print(number_1, "+",number_2,"=", addition(number_1,number_2))
elif choice_operation=='2':
    print(number_1,"-",number_2,"=",substraction(number_1,number_2))
elif choose_operation=='3':
    print(number_1,"/",number_2,"=",division(number_1,number_2))
elif choose_operation=='4':
    print(number_1,"*",number_2,"=",multiplicatrion(number_1,number_2))
else:
    print("invalid input")


