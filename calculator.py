"""A simple command-line calculator."""


def calculate(first_number, operator, second_number):
    """Return the result of applying operator to two numbers."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError(f"Unsupported operator: {operator}")


def main():
    print("Python Calculator")
    print("Supported operators: +, -, *, /")
    print("Enter q to quit.")

    while True:
        expression = input("\nCalculation (number operator number): ").strip()
        if expression.lower() == "q":
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Enter a calculation like: 12 * 3")
            continue

        try:
            first_number = float(parts[0])
            operator = parts[1]
            second_number = float(parts[2])
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result:g}")
        except ValueError as error:
            print(f"Invalid calculation: {error}")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()