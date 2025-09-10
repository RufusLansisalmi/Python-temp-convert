

def main():
    print("This is the main function of temperatur.py")

def print_menu():
   print(f"convert from {from_unit} to {to_unit}")

def get_menu_choice():
    choice = input("Enter your choice: ")
    return choice

def get_unit():
    unit = input("Enter the unit (C/F/K): ")
    return unit
def convert_temperature(get_unit, get_temperature, covert_to_celsius, convert_to_target, print_result):
        from_unit = get_unit()
        to_unit = get_unit()
        temp = get_temperature()
        temp_celsius = covert_to_celsius(temp, from_unit)
        converted_temp = convert_to_target(temp_celsius, to_unit)
        print_result(temp, from_unit, converted_temp, to_unit)
    
def get_temperature(): 
    temp = float(input("Enter the temperature to convert: "))
    return temp
def covert_to_celsius(temp, from_unit):
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