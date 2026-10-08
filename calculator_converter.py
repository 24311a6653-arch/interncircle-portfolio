def arithmetic():
    print("\n--- Arithmetic Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers.")

    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Choose an operation (1-4): ")

        if choice == "1":
            print("Result:", num1 + num2)
            break
        elif choice == "2":
            print("Result:", num1 - num2)
            break
        elif choice == "3":
            print("Result:", num1 * num2)
            break
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)
            break
        else:
            print("Invalid choice! Please choose 1-4.")


def km_to_miles():
    while True:
        try:
            km = float(input("Enter distance in kilometers: "))
            miles = km * 0.621371
            print(f"{km} km = {miles:.2f} miles")
            break
        except ValueError:
            print("Invalid input! Please enter a number.")


def celsius_to_fahrenheit():
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
            break
        except ValueError:
            print("Invalid input! Please enter a number.")


def currency_conversion():
    while True:
        try:
            usd = float(input("Enter amount in USD: "))
            inr = usd * 83
            print(f"{usd} USD = ₹{inr:.2f} INR")
            break
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        print("\n===== Interactive Calculator & Unit Converter =====")
        print("1. Arithmetic Calculator")
        print("2. Kilometers to Miles")
        print("3. Celsius to Fahrenheit")
        print("4. USD to INR Currency Conversion")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            arithmetic()
        elif choice == "2":
            km_to_miles()
        elif choice == "3":
            celsius_to_fahrenheit()
        elif choice == "4":
            currency_conversion()
        elif choice == "5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


main()