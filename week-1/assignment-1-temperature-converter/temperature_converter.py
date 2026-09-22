temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == "C":
    fahrenheit = (temp * 9 / 5) + 32
    kelvin = temp + 273.15
    print(f"{temp}°C = {fahrenheit}°F")
    print(f"{temp}°C = {kelvin}K")

elif unit == "F":
    celsius = (temp - 32) * 5 / 9
    kelvin = celsius + 273.15
    print(f"{temp}°F = {celsius}°C")
    print(f"{temp}°F = {kelvin}K")

elif unit == "K":
    celsius = temp - 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{temp}K = {celsius}°C")
    print(f"{temp}K = {fahrenheit}°F")

else:
    print("Invalid unit! Please enter C, F, or K.")
