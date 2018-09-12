#bitcoin to dollar converter
# print statement notifying the user of the time and date of the conversion standard we are using, then asks for input 
print("As of 9/11/2018 at 7:00pm, bitcoin is currently trading at $6,289.85 per bitcoin.")
amountInBitcoin = float(input("Enter the bitcoin amount:"))

# process for Dollars to Bitcoin
amountInDollars = (amountInBitcoin * 6289.85)

# print the converted amount in U.S. Dollars to the user 
print("That is worth " + format(amountInDollars, ".2f") + " U.S. Dollars")
