class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        else:
            return self.num1 / self.num2


while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    calc = Calculator(num1, num2)

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        print(num1, "+", num2, "=", calc.add())

    elif choice == '2':
        print(num1, "-", num2, "=", calc.subtract())

    elif choice == '3':
        print(num1, "*", num2, "=", calc.multiply())

    elif choice == '4':
        print(num1, "/", num2, "=", calc.divide())

    elif choice == '5':
        break

    else:
        print("Invalid input")
