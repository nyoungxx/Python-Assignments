# Basic Arithmetic Program

# Function to perform arithmetic operations
def arithmetic_program(first_num, second_num):
    # Perform arithmetic operations
    addition = first_num + second_num
    subtraction = first_num - second_num
    multiplication = first_num * second_num

    # Handle division carefully to avoid division by zero
    if second_num != 0:
        division = first_num / second_num
    else:
        division = None

    # Return results
    return {
        "Addition": round(addition, 2),
        "Subtraction": round(subtraction, 2),
        "Multiplication": round(multiplication, 2),
        "Division": round(division, 2) if division is not None else "Cannot divide by zero!"
    }

# Prompt the user for two numbers
try:
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values only.")
    exit()

# Run the arithmetic function and get results
results = arithmetic_program(first_num, second_num)

# Output results with clear labels
print("\nArithmetic Results:")
for operation, result in results.items():
    print(f"{operation}: {result}")

# Example with pre-defined inputs (for demonstration/testing)
print("\nExample Run with Inputs 10 and 3:")
example_results = arithmetic_program(10, 3)
for operation, result in example_results.items():
    print(f"{operation}: {result}")
    