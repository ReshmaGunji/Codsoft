def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter operation choice (1/2/3/4): "))
        if choice < 1 or choice > 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
            return
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print("Result:", result)
        elif choice == 2:
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == 3:
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == 4:
            result = divide(num1, num2)
            print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if _name_ == "_main_":
    main()
