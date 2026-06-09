'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Score Calculator
Description: A simple program that calculates the score of a candidate based on their skills

'''
def score_calculator(python, aws):
    score = 0

    if python == "yes":
        score += 10

    if aws == "yes":
        score += 10

    return score

if __name__ == "__main__":
    python = input("Do you know Python? (yes/no): ")
    aws = input("Do you know AWS? (yes/no): ")

    print("Resume Score:", score_calculator(python, aws))
