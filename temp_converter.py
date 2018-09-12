# Celsius to Fahrenheit
# Fahrenheit = Celsius * 9/5 + 32
# Celsius = (Fahrenheit - 32) * 5/9
# Test points 32 Fahrenheit = 0 Celsius, 212 Fahrenheit = 100 Celsius

# asks for Celcius
tempInCelcius = int(input("Enter a temperature in Celcius: "))

# process for C -> F
tempInFahrenheit = (tempInCelcius * (9.0/5.0)) + 32

print("Temperature: " + str(tempInCelcius) + " Celcius = " + format(tempInFahrenheit, ".2f") + " Fahrenheit")