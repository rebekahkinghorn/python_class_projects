# Name: Rebekah Kinghorn
# Assignment 3: BMI. This calculates BMI based on input

#prompt for first name 
fName = input("Enter your first name: ")

#prompt for last name 
lName = input("Enter your last name: ")

#prompt for feet 
feet = int(input("Enter the feet of your height: "))

#prompt for inches
inches = int(input("Enter the inches of your height: "))

#prompt for weight
weight = int(input("Enter your weight in pounds: "))

#calc total height in inces
totalInches = (feet*12) + inches

#calc bmi
bmi = round((weight / (totalInches**2)*703),2)

#print(bmi)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"


print(f"{fName} {lName} has a BMI of {bmi}. "
       f"The associated category is: {category}.")

#did it submit?