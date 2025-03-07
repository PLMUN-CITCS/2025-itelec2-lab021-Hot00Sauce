def get_non_negative_integer():
    while True: 
        try:
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print(f"The number must be non-negative. Please try again.")
            else:
                return number
        except ValueError: 
            print(f"Invalid input. Please enter an integer.")

def calculate_factorial(number):
    if number == 0:
        return 1
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i 
    return factorial

def main():
    number = get_non_negative_integer()
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number} is: {factorial_result}")  # Indented correctly

if __name__ == "__main__":
    main()
