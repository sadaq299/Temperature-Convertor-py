def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

def main():
    while True:
        print("\nTemperature Conversion Menu:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{f} Fahrenheit is equal to {c:.2f} Celsius")
        elif choice == '2':
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{c} Celsius is equal to {f:.2f} Fahrenheit")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
