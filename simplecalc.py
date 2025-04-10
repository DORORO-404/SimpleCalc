# ===== SimpleCalc Advanced Calculator =====

import pyfiglet

# ANSI Escape Codes for color formatting
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

# Show fancy banner using pyfiglet
def print_banner():
    ascii_banner = pyfiglet.figlet_format("SimpleCalc")
    print(f"{MAGENTA}{ascii_banner}{RESET}")
    box = f"""{CYAN}
  ╔═══════════════════════════════════════╗
  ║     {MAGENTA}SimpleCalc - Advanced Calculator{CYAN}  ║
  ║     {MAGENTA}Developed by: DORORO{CYAN}              ║
  ║     {MAGENTA}Github: DORORO-404{CYAN}                ║
  ║     {MAGENTA}Version: 1.0{CYAN}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# Display the calculator title in styled format
def print_title():
    print(f"{RED}[+] ====== {BLUE}Welcome To SimpleCalc Advanced Calculator {RED}====== [+]{RESET}")

# Get the first number from the user with input validation
def get_first_number():
    while True:
        try:
            return float(input(f"{YELLOW}Enter the first number: {RESET}"))
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a numeric value.{RESET}")

# Get the operation type (+, -, *, /) from the user
def get_operation():
    while True:
        op = input(f"{YELLOW}Enter operation type (+, -, *, /): {RESET}")
        if op in ("+", "-", "*", "/"):
            return op
        else:
            print(f"{RED}❌ Invalid operator. Please enter one of (+, -, *, /).{RESET}")

# Get the second number with zero division check for division
def get_second_number(op):
    while True:
        try:
            num = float(input(f"{YELLOW}Enter the second number: {RESET}"))
            if op == "/" and num == 0:
                raise ZeroDivisionError
            return num
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a numeric value.{RESET}")
        except ZeroDivisionError:
            print(f"{RED}❌ Cannot divide by zero. Please enter another number.{RESET}")

# Perform the calculation and display the result
def show_result(num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    print(f"{GREEN}✅ Result: {num1} {op} {num2} = {result}{RESET}")

# Ask the user if they want to perform another calculation
def ask_user():
    while True:
        choice = input(f"\n{YELLOW}Do you want to perform another operation? [Y/n]: {RESET}").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            print(f"{GREEN}👋 Thank you for using SimpleCalc. Have a great day!{RESET}")
            return False
        else:
            print(f"{RED}❌ Invalid input. Please enter 'y' (yes) or 'n' (no).{RESET}")

# Main function to control the program flow
def main():
    print_banner()
    print_title()
    while True:
        num1 = get_first_number()
        op = get_operation()
        num2 = get_second_number(op)
        show_result(num1, op, num2)
        if not ask_user():
            break

if __name__ == "__main__":
    main()
