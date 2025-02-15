# Exceptional Weather Forecast

# Task 1: Start

while True:
    try:
        user_input = (input("Enter a temperature in Fahrenheit (number only): "))
        temperature = int(user_input)
    except ValueError:
        print(f"'{user_input}' is an invalid number. Please try again. ex: 30")
    else:
        break

# Task 2: Temperature Conversion

def temp_conversion(temperature):
    try:
        temp_subtract = temperature - 32
        temp_multiply = temp_subtract * 5
        temp_celsius = temp_multiply / 9
        celsius = round(temp_celsius, 2)
    except TypeError:
        print("An unexpected TypeError has occurred.")

    # Task 3: User Experience

    else:
        print(f"{temperature} degrees Fahrenheit is {celsius} degrees Celsius.")
    
    # Task 4: Finally

    finally:
        print("Thank you for using the Weather Forecast Converter.")

temp_conversion(temperature)