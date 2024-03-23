operators = ["+", "-", "*", "/","**", "//", "%" ]
cont = "yes"

while cont == "yes":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    for i, operator in enumerate(operators):
        print(f"{i+1}. {operator}")

    operator_index = int(input("Enter the index of the operator you want to use: ")) - 1
    operator = operators[operator_index]

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "**":
        result = num1 ** num2
    elif operator == "//":
        result = num1 // num2
    elif operator == "%":
        result = num1 % num2
    else:
        result = num1 / num2

    print(f"Result: {result}")

    cont = input("Do you want to continue (yes/no)? ").lower()

print("Thanks for using the calculator!")