from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation

number_1 = get_user_number()
operation = get_operation()
number_2 = get_user_number()

sum_result = add(5, 4)
print("5+4=", sum_result)

difference_result = subtract(5, 4)
print("5-4=", difference_result)

product_result = multiply(5, 4)
print("5*4=", product_result)

quotient_result = divide(5, 4)
print("5/4=", quotient_result)

if operation == "+":
    result = add(number_1, number_2)
    print(f"{number_1} + {number_2} = {result}")
elif operation == "-":
    result = subtract(number_1, number_2)
    print(f"{number_1} - {number_2} = {result}")
elif operation == "*":
    result = multiply(number_1, number_2)
    print(f"{number_1} * {number_2} = {result}")
elif operation == "/":
    while number_2 == 0:
        print("Error, cannot divide by zero.")
        number_2 = get_user_number()
    result = divide(number_1, number_2)
    print(f"{number_1} / {number_2} = {result}")

