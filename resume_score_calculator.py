'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Score Calculator
Description: A simple program that calculates the score of a candidate based on their skills

'''
score = 0

python = input("Do you know Python? (yes/no): ")
aws = input("Do you know AWS? (yes/no): ")

if python == "yes":
   score = score + 10

if aws == "yes":
   score = score + 10

print("Resume Score:", score)
