# ===== Advanced Calculator =====

# ANSI Escape Codes for color formatting
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

# Print the title with color
print(f"{RED}[+] ====== {BLUE}Welcome To Advanced Calculator {RED}====== [+]{RESET}")

while True:
    # Input the first number
    while True:
        try:
            first_number = float(input(f"{YELLOW}Enter the first number: {RESET}"))
            break
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a numeric value.{RESET}")

    # Input the operation type
    while True:
        operation = input(f"{YELLOW}Enter operation type (+, -, *, /): {RESET}")
        if operation in ("+", "-", "*", "/"):
            break
        else:
            print(f"{RED}❌ Invalid operator. Please enter one of (+, -, *, /).{RESET}")

    # Input the second number
    while True:
        try:
            second_number = float(input(f"{YELLOW}Enter the second number: {RESET}"))
            if operation == "/" and second_number == 0:
                raise ZeroDivisionError
            break
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a numeric value.{RESET}")
        except ZeroDivisionError:
            print(f"{RED}❌ Cannot divide by zero. Please enter another numeric value.{RESET}")

    # Perform the calculation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number

    print(f"{GREEN}Result Is: {result}{RESET}")

    # Ask the user if they want to perform another operation
    while True:
        ask_user = input(f"{YELLOW}Do you want to perform another operation? [Y/n]: {RESET}").strip().lower()
        if ask_user == "y":
            break
        elif ask_user == "n":
            print(f"{GREEN}Thank you for using the Calculator. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}❌ Invalid input. Please enter 'y' or 'n'.{RESET}")
