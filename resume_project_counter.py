'''
Author: Asmita
Date: 2024-06-01
Feature: Resume Project Counter
Description: A simple program that counts the number of projects in a candidate's resume

'''
def projectCounter():
   projects = int(input("How many projects are in your resume? "))
   
   for i in range(projects):
      project = input("Enter project name: ")
      print("Project added:", project)

projectCounter()
