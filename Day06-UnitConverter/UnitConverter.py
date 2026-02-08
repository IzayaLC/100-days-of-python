def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) / (9/5), 2)
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = round((celsius * 9/5) + 32, 2)
    return fahrenheit

def inches_to_centimeters(inches):
    centimeters = round(inches * 2.54, 2)
    return centimeters

def centimeters_to_inches(centimeters):
    inches = round(centimeters / 2.54, 2)
    return inches

print('Welcome to the Unit Converter. What converter would you like to use?')
converter = input(
"""
Type '1' for Fahrenheit to Celsius. 
Type '2' for Celsius to Fahrenheit. 
Type '3' for Inches to Centimeters. 
Type '4' for Centimeters to Inches. 
""")

if converter == '1':
    fahrenheit = int(input("Enter the temperature in fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"That is {celsius} in celsius.")
    
if converter == '2':
    celsius = int(input('Enter the temperature in celsius: '))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"That is {fahrenheit} in fahrenheit.")
    
if converter == '3':
    inches = int(input("Enter the length in inches: "))
    centimeters = inches_to_centimeters(inches)
    print(f"That is {centimeters} in centimeters.")
    
if converter == '4':
    centimeters = int(input('Enter the length in centimeters: '))
    inches = centimeters_to_inches(centimeters)
    print(f"That is {inches} in inches.")
