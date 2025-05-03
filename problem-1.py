class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str):
        if operation == "add" or operation == "+":
            return self.a + self.b
        elif operation == "subtract" or operation == "-":
            return self.a - self.b
        elif operation == "multiply" or operation == "*":
            return self.a * self.b
        elif operation == "divide" or operation == "/":
            if self.b == 0:
                return "Oops! You can't divide by zero"
            return self.a / self.b
        else:
            return "Sorry, that operation is not supported."


if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            operation = input("Enter operation (add(+), subtract(-), multiply(*), divide(/)): ").strip().lower()

            calc = Calculator(a, b)
            result = calc.calculate(operation)
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numbers for a and b.")

        # Ask if the user wants to continue
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Thank you for using the calculator!")
            break
