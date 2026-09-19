# Name:
# 

#welcome function
def welcome_message(name:str):
    print(f"Hello {name}, welcome to IS 303!")

welcome_message("Diego")
welcome_message("Mai")


import a6_my_functions


#call sum function #2
print(a6_my_functions.sum_two_numbers(5,7))
print(a6_my_functions.sum_two_numbers(1000.5,-30))

#call is even function #3
print(a6_my_functions.is_even(7))
print(a6_my_functions.is_even(120))


#call parity funciton #4
print(a6_my_functions.get_number_parity(5))
print(a6_my_functions.get_number_parity(10))


#call degrees function #5
print(a6_my_functions.fahrenheit_to_celsius(32))
print(a6_my_functions.fahrenheit_to_celsius(75))


#call min max mean function #6
numbers_list_1 = [20, 45, 23, 2, 87, 3]
print(a6_my_functions.min_max_mean(numbers_list_1))


#call dog function #7
print(a6_my_functions.dog_message("Spot",7))
print(a6_my_functions.dog_message("Peppy"))


#call age function #8
print(a6_my_functions.classify_age(60,55))
print(a6_my_functions.classify_age(62))


#call price function #9
counter = 1
while counter <= 2:
    my_price = int(input("Enter the price for the product purchased: "))
    my_quantity = int(input("Enter the quantity of the product purchased: "))
    my_discount_percent = float(input("Enter the discount percent (formatted as a decimal): "))

    print(f"The total price after discounts is: ${a6_my_functions.calculate_total(my_price,my_quantity,my_discount_percent)}")
    counter += 1


