import art
import os

print(art.logo)

#functions 
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if(n2 == 0):
        return "Can not divide by zero"
    return float(n1/n2)


operationDict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def calculator(num1, num2, exp):
    function = operationDict[exp]
    return function(num1, num2)


exitCal = False
while not exitCal:
    num1 = float(input("Enter a number: "))
    for i in operationDict:
        print(i)
    exp = input("Choose an expression from the given list \n ")
    num2 = float(input("Enter a number: "))

    result = calculator(num1, num2, exp)
    print(f"{num1} {exp} {num2} = {result}")

    askCont = input(f"Type y to continue with {result}, or type n to start a new calculation \n").lower()
    if askCont=="y":
        askToContinue = True
    else:
        askToContinue = False

    while askToContinue:
        num1 = result
        for i in operationDict:
            print(i)
        exp = input("Choose an expression from the given list \n ")
        num2 = float(input("Enter the next number: ")) 
        result = calculator(num1, num2, exp)
        print(f"{num1} {exp} {num2} = {result}")
        askCont = input(f"Type y to continue with {result}, or type n to start a new calculation \n").lower()
        if askCont=="n":
            askToContinue = False

            
    os.system("cls")    
    print(art.logo)

