#!/usr/bin/env python3


# Create a simple calculator that can add, subtract, multiply, and divide.

# Note: These examples are built on Python 3.9 which does not have match/case

def switch(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b

if __name__ == "__main__":
    print("simple calculator")
    first_num = int(input("first number:"))
    second_num = int(input("second number:"))
    oper = input("operator:")

    answer = switch(oper, first_num, second_num)

    print(answer)
