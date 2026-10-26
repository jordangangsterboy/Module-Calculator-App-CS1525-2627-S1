def get_user_number() -> float:
    """asks the user for an input and validates it"""
    while True:
        try:
            return float(input("Type in a number: "))
        except ValueError:
            print("Invalid, please try again.")

def get_operation() -> str:
    """asks the user for an operation sign and validates it"""
    while True:
        operation = input("Type in an operation (+, -, *, /): ")
        if operation in ("+", "-", "*", "/"):
            return operation
        print("Invalid, please try again and enter +, -, *, or /.")

