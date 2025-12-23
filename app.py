"""
Simple Calculator Program
-------------------------
This program performs basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

Features:
- Uses functions for reusability
- Handles division by zero safely
- Validates user input
- Well-documented for beginners
"""

def get_number(prompt):
    """
    Takes user input and ensures it is a valid number.
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Returns the division result.
    Handles division by zero safely.
    """
    if b == 0:
        return "❌ Error: Cannot divide by zero"
    return a / b


def main():
    """
    Main function to run the calculator.
    """
    print("📌 Simple Calculator")
    print("--------------------")

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("\nResults:")
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))


# Program entry point
if __name__ == "__main__":
    main()
