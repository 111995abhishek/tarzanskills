
def addition(number_1,number_2):
    sum = number_1 + number_2
    return sum




def substraction(number_1,number_2):
    diffrence=number_1-number_2
    return diffrence



def multiplication(number_1,number_2):
    product=number_1*number_2
    return product


def division(number_1,number_2):
    quotient=number_1+number_2
    return quotient
while(True):

    number_1=int(input("enter the number_1"))
    number_2=int(input("enter the number_2"))
    operation = input("enter the opeartion to be performed")
    if operation=='addition':
        print(f"the sum  of{number_1} and {number_2} is " ,addition(number_1,number_2))
    elif operation=='substraction':
              print(f"the diference of{number_1} and {number_2} is",substraction(number_1,number_2))
    elif operation=='multiplication':
        print(f"the product of {number_1} and {number_2} is",multiplication(number_1,number_2))
    elif operation=='division':
        print(f"the quotient of {number_1} and {number_2} is",division(number_1,number_2))
    else:
        print("invalid operation")
        break






