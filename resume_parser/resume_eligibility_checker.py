'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Eligibility Checker
Description: A simple program that checks the eligibility of a candidate for different developer roles based on their

'''

def eligibility_checker(experience):
    if experience >= 5:
        return "Senior Developer"
    elif experience >= 2:
        return "Mid-Level Developer"
    elif experience >= 0:
        return "Junior Developer"
    else:
        return "Not Eligible"


# Optional manual run (for local testing)
if __name__ == "__main__":
    name = input("Enter your name: ")
    experience = int(input("Enter years of experience: "))

    role = eligibility_checker(experience)
    print(f"{name} is eligible for: {role}")