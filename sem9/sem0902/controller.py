from operation import Operation
from logger import Logger

class Controller:
    def __init__(self):
        self.operation = Operation()
        self.logger = Logger("calculator.log")

    def run(self):
        print("Welcome to the calculator!")
        while True:
            print("\nPlease choose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Complex Add")
            print("6. Complex Subtract")
            print("7. Complex Multiply")
            print("8. Complex Divide")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                self.add()
            elif choice == "2":
                self.subtract()
            elif choice == "3":
                self.multiply()
            elif choice == "4":
                self.divide()
            elif choice == "5":
                self.complex_add()
            elif choice == "6":
                self.complex_subtract()
            elif choice == "7":
                self.complex_multiply()
            elif choice == "8":
                self.complex_divide()
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add(self):
        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")
        result = self.operation.add(num1, num2)
        self.display_result(result)

    def subtract(self):
        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")
        result = self.operation.subtract(num1, num2)
        self.display_result(result)

    def multiply(self):
        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")
        result = self.operation.multiply(num1, num2)
        self.display_result(result)

    def divide(self):
        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")
        result = self.operation.divide(num1, num2)
        self.display_result(result)

    def complex_add(self):
        num1 = self.get_complex_number("Enter the first complex number (in the format a+bj): ")
        num2 = self.get_complex_number("Enter the second complex number (in the format a+bj): ")
        result = self.operation.complex_add(num1, num2)
        self.display_complex_result(result)

    def complex_subtract(self):
        num1 = self.get_complex_number("Enter the first complex number (in the format a+bj): ")
        num2 = self.get_complex_number("Enter the second complex number (in the format a+bj): ")
        result = self.operation.complex_subtract(num1, num2)
        self.display_complex_result(result)

    def complex_multiply(self):
        num1 = self.get_complex_number("Enter the first complex number (in the format a+bj): ")
        num2 = self.get_complex_number("Enter the second complex number (in the format a+bj): ")
        result = self.operation.complex_multiply(num1, num2)
        self.display_complex_result(result)

    def complex_divide(self):
        num1 = self.get_complex_number("Enter the first complex number (in the format a+bj): ")
        num2 = self.get_complex_number("Enter the second complex number (in the format a+bj): ")
        result = self.operation.complex_divide(num1, num2)
        self.display_complex_result(result)

    def get_number(self, message):
        number_str = input(message)
        try:
            number = float(number_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
            number = self.get_number(message)
        return number

    def get_complex_number(self, message):
        complex_number_str = input(message)
        try:
            complex_number = complex(complex_number_str)
        except ValueError:
            print("Invalid input. Please enter a complex number in the format a+bj.")
            complex_number = self.get_complex_number(message)
        return complex_number

    def display_result(self, result):
        print("Result: {0}".format(result))
        self.logger.log("Result: {0}".format(result))

    def display_complex_result(self, result):
        print("Result: {0} + {1}j".format(result.real, result.imag))
        self.logger.log("Result: {0} + {1}j".format(result.real, result.imag))

if __name__ == "__main__":
    controller = Controller()
    controller.run()
