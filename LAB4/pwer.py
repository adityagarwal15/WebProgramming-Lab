class Power:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def my_pow(self):
        result = 1
        # Handle negative exponent
        if self.exponent < 0:
            self.base = 1 / self.base
            self.exponent = -self.exponent
        
        # Loop to multiply the base 'exponent' times
        for _ in range(self.exponent):
            result *= self.base
        return result

# Taking input from the user
x = float(input("Enter the base (x): "))  # Base (x)
n = int(input("Enter the exponent (n): "))  # Exponent (n)

# Creating an instance of Power class
power_calculator = Power(x, n)

# Calculating the result
result = power_calculator.my_pow()

# Displaying the result
print(f"The result of {x}^{n} is: {result}")
