'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Experience Analyzer
Description: A simple program that analyzes the years of experience of a candidate and classifies them as
'''
def resume_experience_analyzer():
    experience = int(input("Please enter your years of experience: "))
    if experience < 1:
        print("Fresher")
    elif experience <= 3:
        print("Junior Developer")
    elif experience <= 6:
        print("Mid-Level Developer")
    else:
        print("Senior Developer")

resume_experience_analyzer()
