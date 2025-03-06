# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RPathak,2/28/2025,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Class FileProcessor :reads and writes data to and from json file |Data processing Layer
class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, students: list): # function to read data from json file and stores to student list
        try:
            file = open(FILE_NAME, "r")
            students = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)
        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, students: list): # write data to from students (dictionary) to json file
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following student data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                        f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

class IO: #    class to show program output  | Presentation Layer
    @staticmethod
    def output_error_messages(message: str, error: Exception =None):   #function to display error messages
        print(message)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu:str):   # function to display menu
        print(MENU)

    @staticmethod
    def input_menu_choice():    # function to take user input
        menu_choice = input("What would you like to do: ")
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):  #function to display student data
        print("-" * 50)
        for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
    @staticmethod
    def input_student_data(student_data: list):  # function to collect data to studet_data list
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data.append({"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name
            })
            print("-" * 50)
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        except ValueError as e:
            IO.output_error_messages("Invalid input. Names should not contain numbers.", e)


# Main Program
while (True):

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # processing as per menu choice

    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(students)
    elif menu_choice == "2":  # Show current data
        IO.output_student_courses(students)
    elif menu_choice == "3":  # Save data to file
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":  # Exit the program
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
