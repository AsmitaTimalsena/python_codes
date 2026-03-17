'''
author: Asmita Timalsena
date: 2026-03-17
feature: Resume Parser
description: A simple resume parser that takes user input for various fields such as name, bio, email, phone number, address, headline, photo image URL, and resume URL.
implementation: This code is a simple resume parser that takes user input for various fields such as name, bio, email, phone number, address, headline, photo image URL, and resume URL. It then prints out the parsed information in a formatted manner.
'''
resumes = []
while True:
    print("Welcome to the Resume Parser!")
    print("Please enter the following information:")
    
    name = input("Name: ")
    bio = input("Bio: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    skill_input = input("Skill: ")
    photo_image_url = input("Photo Image URL: ")
    Experience = input("Experience: ")
    resume_url = input("Resume URL: ")
    skill = [s.strip().lower() for s in skill_input.split(",")]
    individual_resume = [name, email, skill, Experience]
    resumes.append(individual_resume)
    cont = input("\nDo you want to parse another resume? (yes/no): ")
    if cont.lower() != 'yes':
        break

dct_resumes = {}

for i in range(len(resumes)):
    name = resumes[i][0]
    dct_resumes[name] = resumes[i][1:]

all_skills = []
for skill in resumes:
    all_skills.extend(skill[2])

unique_skills = set(all_skills)
print("Unique Skills:", unique_skills)


# Define required skills using a tuple
required_skills = ("python", "sql", "data analysis", "communication")

# match each candidate based on required skills
matched_candidates = []

for name, value in dct_resumes.items():
    skills = value[1]

    matched = []
    for s in skills:
        if s in required_skills:
            matched.append(s)


    matched_candidates.append((name, matched))

print("Matched Candidates:")
for candidate in matched_candidates:
    print("Name:", candidate[0])
    print("Skills:", candidate[1] if candidate[1] else "No matching skills")
    print() 
