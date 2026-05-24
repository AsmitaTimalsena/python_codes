'''
Create a menu driven program in python which takes student data from input, show the data, update it and delete it , 
The data must contain 
Name, dob, roll no , level of education, address, 
The program must be based on the class
'''

class Student:
    def __init__(self, name, dob, roll_no, education_level, address):
        self.name = name
        self.dob = dob
        self.roll_no = roll_no
        self.education_level = education_level
        self.address = address

    def show_data(self):
        print("Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Roll No:", self.roll_no)
        print("Education Level:", self.education_level)
        print("Address:", self.address)

    def update_data(self, name=None, dob=None, roll_no=None, education_level=None, address=None):
        if name:
            self.name = name
        if dob:
            self.dob = dob
        if roll_no:
            self.roll_no = roll_no
        if education_level:
            self.education_level = education_level
        if address:
            self.address = address

    def delete_data(self):
        del self.name
        del self.dob
        del self.roll_no
        del self.education_level
        del self.address


name = input("Enter student name: ")
dob = input("Enter date of birth:(DD-MM-YYYY) ")
roll_no = input("Enter roll number: ")
education_level = input("Enter level of education:(eg: Bachelor's, Master's) ")
address = input("Enter address: ")


while True:

    student_info = Student(name, dob, roll_no, education_level, address) 
    print("\n What action do you want to perform? ")
    print("1. Show Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Exit")
    user_choice = input("Enter your choice:(1-4) ")
    if user_choice == '1':
        student_info.show_data()
    elif user_choice == '2':
        new_name = input("Enter new name (leave blank to keep current): ")
        new_dob = input("Enter new date of birth (leave blank to keep current): ")
        new_roll_no = input("Enter new roll number (leave blank to keep current): ")
        new_education_level = input("Enter new level of education (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")
        student_info.update_data(new_name, new_dob, new_roll_no, new_education_level, new_address)
    elif user_choice == '3':
        student_info.delete_data()
        print("Data deleted successfully!")
    elif user_choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.") 
    
