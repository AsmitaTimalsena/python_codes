'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Eligibility Checker
Description: A simple program that checks the eligibility of a candidate for different developer roles based on their

'''
def eligibilty_checker():
    name = input("Please enter your name: ")
    experience = int(input("Please enter your years of experience: "))
    
    if experience >= 5:
        print(name, " is eligible for the role of Senior Developer.")
    elif experience >= 2 and experience < 5:
        print(name, " is eligible for the role of Mid-Level Developer.")
    elif experience >= 0 and experience < 2:
        print(name, " is eligible for the role of Junior Developer.")
    else:
        print(name, " is not eligible for any of the specified roles.")


eligibility_checker()
