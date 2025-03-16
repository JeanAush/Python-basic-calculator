

"""
Get the user's numbers and operation
"""
def main():


    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number: "))
    operation = input("Enter the mathematical operation (+, -, *, /): ")
    

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result  = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Division by zero ain't allowed!"
        else:
            result = num1 /num2
    else:
        result = "Invalid Operation. Please try again."
        return

    print("The answer is: ", result)




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()