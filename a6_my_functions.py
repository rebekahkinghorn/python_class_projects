# Name:
# contains functions 2-the end


#2. sum function 
def sum_two_numbers(a,b):
    return a+b


#3. is even function
def is_even(num:int):
    if num % 2 == 0:
        return True
    else:
        return False


#4. number parity
def get_number_parity(num):
    #return f"is_even(num)"
    if is_even(num) == True:
        return f"{num} is even."
    else:
        return f"{num} is odd."


#5. fahrenheit_to_celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius


#6. min_max_mean
def min_max_mean(numbers_list):
    numbers_list.sort()
    #print(numbers_list)
    min = numbers_list[0]
    max = numbers_list[len(numbers_list)-1]
    
    num_sum = 0
    for num in numbers_list:
        num_sum += num

    mean = num_sum / len(numbers_list)
    return [min, max, mean]


#7. dog_message
def dog_message(name:str, age:int = 0):
    return f"I am a dog named {name} and I'm {age} years old!"


#8. classify_age
def classify_age(age:int, senior_age:int =65):
    if age < 18:
        return "Minor"
    elif age < senior_age:
        return "Adult"
    else:
        return "Senior"


#9. calculate_total
def calculate_total(price, quantity:int, discount_percent:float, threshold_total = 100, bonus_discount = 0.02):
    total_price = price * quantity
    if total_price <= threshold_total:
        final_price = round(total_price * (1 - discount_percent),1)
    else:
        final_price = round(total_price * (1 - discount_percent - bonus_discount),1)
    return final_price