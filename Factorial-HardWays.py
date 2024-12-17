# First, we need to make the function
# Factorial function using a for loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# We take the Input from the user
num = int(input("Enter a number to calculate its factorial: "))

# And then, Calculating factorial
fact = factorial(num)

# The Result!
print(f"The factorial of {num} is {fact}")
