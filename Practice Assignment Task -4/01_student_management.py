# Program: Student Management System

# Create a Student class
# Display student details and calculate grade

class Student:

    def __init__(self, name, roll_number, marks):

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        else:
            return "C"

    def display_details(self):

        print("\nStudent Details")

        print("Name :", self.name)

        print("Roll Number :", self.roll_number)

        print("Marks :", self.marks)

        print("Grade :", self.calculate_grade())


student1 = Student("Rajat", 101, 98)

student1.display_details()
