def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y != 0:
        return x / y
    else:
        return "Number cannot be divide by zero"

while True:
    print("Select operation you want to perform :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exit the calculator.")
        break

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == '1':
        print(number1, "+", number2, "=", addition(number1, number2))
    elif choice == '2':
        print(number1, "-", number2, "=", subtraction(number1, number2))
    elif choice == '3':
        print(number1, "*", number2, "=", multiplication(number1, number2))
    elif choice == '4':
        print(number1, "/", number2, "=", division(number1, number2))
    else:
        print("Invalid input")
