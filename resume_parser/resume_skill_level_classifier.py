'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Skill Level Classifier
Description: A simple program that classifies a candidate's skill level based on the number of programming skills they know

'''
def skillClassifier():
    skills = int(input("How many programming skills do you know? (enter in numbers) "))
    
    if skills >= 5:
        print("You are an Expert in programming skills.")
    elif skills >= 3 and skills < 5:
        print("You are an Intermediate in programming skills.")
    elif skills >= 0 and skills < 3:
        print("You are a Beginner in programming skills.")
    else:
        print("Invalid input. Please enter a non-negative number.")

skillClassifier()
