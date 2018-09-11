# Fahrenheit to Celsius
# Fahrenheit = Celsius * 9/5 + 32
# Celsius = (Fahrenheit - 32) * 5/9
# Test points 32 Fahrenheit = 0 Celsius, 212 Fahrenheit = 100 Celsius

# asks for Fahrenheit
tempInFahrenheit = int(input("Enter a temperature in Fahrenheit: "))

# process for F -> C
tempInCelsius = (tempInFahrenheit - 32) * 5.0/9.0

print("Temperature: " + str(tempInFahrenheit) + " Fahrenheit = " + format(tempInCelsius, ".2f") + " Celsius")