from art import logo


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

operations = {"+": add,
            "-": substract, 
            "*": multiply, 
            "/": divide,
            "**": exponent
            }

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for i in operations:
        print(i)

    should_continue = True

    while should_continue:

        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))  
        calculation_function = operations[operator]
        result = calculation_function(num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'e' to exit.: ")

        if cont == "y":
            num1 = result
        elif cont == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()
