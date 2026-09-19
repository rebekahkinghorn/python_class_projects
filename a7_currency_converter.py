# Name: Rebekah Kinghorn
# This is a currency converter to practice exception handling. 

# I'm providing you with this dictionary. Use this in writing your code.
conversion_rates = { 
    "EUR": 0.93, # Euro 
    "GBP": 0.81, # British Pound 
    "JPY": 133.0, # Japanese Yen 
    "INR": 82.5, # Indian Rupee 
    "AUD": 1.48, # Australian Dollar 
    "CAD": 1.36, # Canadian Dollar 
    "CHF": 0.92, # Swiss Franc 
    "CNY": 7.15, # Chinese Yuan 
    "SEK": 10.5, # Swedish Krona 
    "NZD": 1.62, # New Zealand Dollar 
    "MXN": 18.0, # Mexican Peso 
} 

#the outer try
try:

    #begin a loop to get inputs until we get a valid dollar amount
    find_amount = True
    while find_amount:

        #try to get inputs and throw an error if they don't enter a floatable number
        try:
            og_amount = input("Enter an amount in US dollars: ")
            amount = float(og_amount)
            rounded_amount = round(amount,2)
            find_amount = False
        except ValueError:
            print(f"\"{str(og_amount)}\" is not a valid number. Please try again.")

    
    #print da money list
    print("Foreign currencies available for conversion are:")
    
    for money_key,money_value in conversion_rates.items():
        print(money_key, end=" ")
    
    print()
        

    #function to use the target currency and return the converted amount of money
    def convert(target):
        returned_currency = conversion_rates[target] * amount
        returned_currency_rounded = round(returned_currency, 2)
        return returned_currency_rounded


    #start a loop to get inputs until we get a valid currency
    ask_for_currency = True
    while ask_for_currency:

        #try to get a valid currency
        try:
            target_currency = input("Please enter a target currency (e.g., EUR, GBP): ").strip().upper()
            final_value = convert(target_currency)
            ask_for_currency = False
        except KeyError:
            print(f"{target_currency} is not a valid currency. Please try again.")


    #print the final statement! :)
    print(f"{rounded_amount} USD is equal to {final_value} {target_currency}")
    
except Exception as e:
    print(f"\nError: {e}\n")