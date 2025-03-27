print("----------Welcome To Calculator Program----------")
while True:
# Input the first number
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Input the operation type
    while True:
        operation = input("Enter operation type (+, -, *, /): ")
        if operation in ("+", "-", "*", "/"):
            break
        else:
            print("Invalid operator. Please enter one of (+, -, *, /).")

# Input the second number
    while True:
        try:
            second_number = float(input("Enter the second number: "))
            if operation == "/" and second_number == 0:
                raise ZeroDivisionError
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter another numeric value.")

# Perform the calculation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number

    print("Result Is", result)

# Ask the user if they want to perform another operation
    while True:
        ask_user = input("Do you want to perform another operation? [y/n]: ").lower()
        if ask_user == "y":
            break
        elif ask_user == "n":
            print("Program exited.")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")