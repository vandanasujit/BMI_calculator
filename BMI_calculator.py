#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#weight in pounds (lb) * 703 / height in inches (in) squared 
weight = float(input("enter your weight in pounds: "))
height= float(input("enter your height in inches: "))
BMI = weight*703/(height**2)
print(f"your BMI is : {BMI}")
if BMI>0:
    if BMI<18.5:
        print("you are under weight and healthrisk is minimal")
    elif 18.5<=BMI<=24.9:
        print("Normal weight and healthrisk minimal")
    elif 25<=BMI<=29.9:
        print("overweight and healthrisk increased")
    elif 30 <=BMI<= 34.9:
        print("obese and healthrisk high")
    elif 35 <=BMI<=39.9:
        print("severely obese and healthrisk very high")
    elif BMI>=40:
        print("Morbidly obese and health risk extremely high")
else:
    print("invalid inputs")

