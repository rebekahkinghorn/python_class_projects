# Rebekah Kinghorn
# pandas assignment 10 

import os
def clear():
    os.system('cls')

import pandas as pd

#1. import data
practice_names_df = pd.read_csv(r"practice_names.csv")
# print(practice_names_df)


#1.0. access columns
#print city column 
print()
print(practice_names_df["city"])

#print name and age columns in one print stmt
print()
# print(practice_names_df.loc[:,['name','age']])
print(practice_names_df[["name", "age"]])


# 2. update values - see class notes 03 for this topic on a better way to do this 
#change salary of Joey Tribbiani
practice_names_df.iloc[8,3] = 56000
# print()
# print(practice_names_df)

#change the age of Jane Smith
practice_names_df.iloc[1,1] = 29
# print()
# print(practice_names_df)

#print Jane and Joey's info
# clear()
print()
print(practice_names_df.iloc[[8]])
print(practice_names_df.iloc[[1]])


#3. insert columns
practice_names_df.insert(loc=3, column="seniority", value= "")
print()
# print(practice_names_df)


#4. update based on condition
#say "experienced" for all 35 years old and older
practice_names_df.loc[practice_names_df["age"] > 35, "seniority"] = "experienced"
print()
# print(practice_names_df) 



#5. filter
# use .query to find all peeps > 30 y old  AND live in either Seattle or Boston or San Fran
#store as a new df
new_df = practice_names_df.query("(age >= 30) and (city == 'Seattle' or city == 'Boston' or city == 'San Francisco')")
# print()
# print(new_df)



#6. sort 
#sort based on salary in desc order
newer_df = new_df.sort_values("salary", ascending=False)
print()
print(newer_df)


#7. math functions
#print mean of salary column 
print()
print(round(newer_df["salary"].mean(),2))


#8. group by 
#new df grouped by city that shows mean of each city
newest_df = newer_df.groupby("city")["salary"].mean()
print()
print(newest_df)


#9. export to new format
newest_df.to_excel("mean_salary_by_city.xlsx")
