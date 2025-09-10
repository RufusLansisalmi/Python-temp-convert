def main():
    while True:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            convert(get_unit, get_temperature, convert_to_celsius, convert_to_target, print_result)
        elif choice == 2:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print("Temperature Conversion Menu:")
    print("1. Convert temperature")
    print("2. Exit")

def get_menu_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def get_unit(prompt="Enter the unit (C/F/K): "):
    unit = input(prompt).upper()
    if unit in ['C', 'F', 'K']:
        return unit
    else:
        print("Invalid unit. Please enter C, F, or K.")
        return get_unit(prompt)

def convert(get_unit, get_temperature, convert_to_celsius, convert_to_target, print_result):
    from_unit = get_unit("Enter the unit to convert from (C/F/K): ")
    to_unit = get_unit("Enter the unit to convert to (C/F/K): ")
    temp = get_temperature()
    temp_celsius = convert_to_celsius(temp, from_unit)
    converted_temp = convert_to_target(temp_celsius, to_unit)
    print_result(temp, from_unit, converted_temp, to_unit)

def get_temperature(): 
    try:
        temp = float(input("Enter the temperature to convert: "))
        return temp
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_temperature()

def convert_to_celsius(temp, from_unit):
    if from_unit == 'F':
        return (temp - 32) * 5.0/9.0
    elif from_unit == 'K':
        return temp - 273.15
    else:
        return temp

def convert_to_target(temp_celsius, to_unit):
    if to_unit == 'F':
        return (temp_celsius * 9.0/5.0) + 32
    elif to_unit == 'K':
        return temp_celsius + 273.15
    else:
        return temp_celsius

def print_result(original_temp, from_unit, converted_temp, to_unit):
    print(f"{original_temp} {from_unit} is {converted_temp:.2f} {to_unit}")

if __name__ == "__main__":
    main()
