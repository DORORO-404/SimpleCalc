# ========= SimpleCalc - Advanced Calculator =========

# === Import necessary modules ===
import pyfiglet
import sys
import os

# === ANSI colors ===
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# === Version info ===
VERSION = "1.2"

# === Clear screen based on OS ===
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# === Print banner using pyfiglet ===
def print_banner():
    ascii_banner = pyfiglet.figlet_format("  SimpleCalc")
    print(f"{MAGENTA}{ascii_banner}{RESET}")
    box = f"""{CYAN}
  ╔═══════════════════════════════════════╗
  ║     {MAGENTA}SimpleCalc - Advanced Calculator{CYAN}  ║
  ║     {MAGENTA}Developed by: DORORO__404{CYAN}         ║
  ║     {MAGENTA}GitHub: DORORO-404{CYAN}                ║
  ║     {MAGENTA}Version: {VERSION}{CYAN}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# === Show a welcome message ===
def print_title():
    print(f"{RED}[+] ===== {CYAN}Welcome to SimpleCalc Advanced Calculator{RED} ===== [+]{RESET}")

# === Exit safely with a message ===
def exit_program():
    print(f"{GREEN}Exiting SimpleCalc...{RESET}")
    sys.exit()

# === Handle input and check for exit keywords ===
def safe_input(prompt):
    try:
        user_input = input(prompt).strip().lower()
        if user_input in ["exit", "quit", "q", "x", "close"]:
            exit_program()
        return user_input
    except KeyboardInterrupt:
        print(f"\n{GREEN}Exiting SimpleCalc...{RESET}")
        sys.exit()

# === Ask for a number and validate it ===
def get_number(prompt_text):
    while True:
        try:
            return float(safe_input(f"{YELLOW}{prompt_text}{RESET}"))
        except ValueError:
            print(f"{RED}Invalid input. Please enter a numeric value.{RESET}")

# === Ask for an operation from the user ===
def get_operation():
    while True:
        op = safe_input(f"{YELLOW}Enter operation (+, -, *, /): {RESET}")
        if op in ["+", "-", "*", "/"]:
            return op
        else:
            print(f"{RED}Invalid operator. Use one of (+, -, *, /).{RESET}")

# === Ask for second number and avoid division by zero ===
def get_second_number(op):
    while True:
        num = get_number("Enter the second number: ")
        if op == "/" and num == 0:
            print(f"{RED}Cannot divide by zero.{RESET}")
        else:
            return num

# === Perform and display the calculation result ===
def show_result(num1, op, num2):
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    print(f"\n{GREEN}Result: {num1} {op} {num2} = {result}{RESET}")

# === Ask if user wants to calculate again ===
def ask_repeat():
    while True:
        answer = safe_input(f"\n{YELLOW}Do you want to perform another calculation? [Y/n]: {RESET}").lower()
        if answer in ["y", ""]:
            return True
        elif answer == "n":
            return False
        else:
            print(f"{RED}Invalid input. Please enter 'y' or 'n'.{RESET}")

# === Main function to control the program ===
def main():
    # Check version flag
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"{CYAN}SimpleCalc Version: {VERSION}{RESET}")
        sys.exit()

    while True:
        clear_screen()
        print_banner()
        print_title()

        num1 = get_number("Enter the first number: ")
        op = get_operation()
        num2 = get_second_number(op)
        show_result(num1, op, num2)

        if not ask_repeat():
            print(f"{GREEN}Thank you for using SimpleCalc. Goodbye!{RESET}")
            exit()

# === Run the script ===
if __name__ == "__main__":
    main()
