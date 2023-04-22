class Operation:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def complex_add(self, num1, num2):
        real = num1.real + num2.real
        imag = num1.imag + num2.imag
        return complex(real, imag)

    def complex_subtract(self, num1, num2):
        real = num1.real - num2.real
        imag = num1.imag - num2.imag
        return complex(real, imag)

    def complex_multiply(self, num1, num2):
        return num1 * num2

    def complex_divide(self, num1, num2):
        return num1 / num2
