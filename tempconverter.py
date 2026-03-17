# Temperature Converter using functions with return values

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32


# Example usage
c = 25
f = 77
k = 300

print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")
print(f"{f}°F = {fahrenheit_to_kelvin(f):.2f}K")
print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}°F")
