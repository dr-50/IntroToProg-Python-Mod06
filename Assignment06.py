# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Devon Ross,11/16/2026,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Data constants
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

#Variables
menu_choice: str = ""  #user selection from menu
students: list = []    #student table of data


class FileProcessor:
    """
    A collection of functions that process the file data

    ChangeLog: (Who, When, What)
    Devon Ross, 11/16/2026, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str):
        """This function reads data from file

        ChangeLog: (Who, When, What)
        Devon Ross, 11/16/2026, Created function

        :param file_name: string data as file name
        """
        file = None
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            for item in student_data:
                students.append(item)
        except FileNotFoundError as e:
            IO.output_error_message("File must exist before running this program!", e)
        except Exception as e:
            IO.output_error_message("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function writes current data to file

        :param file_name: string data as file name
        :param student_data: list of dictionaries as student data
        """
        file = open(FILE_NAME, "w")
        json.dump(students, file, indent=4)

        # check if a file object exists and is still open
        if file is not None and file.closed == False:
            file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in "
                  f"{student['CourseName']}")

class IO:
    """
    A collection of functions that handle input output

    ChangeLog: (Who, When, What)
    Devon Ross, 11/16/2026, Created Class
    """

    @staticmethod
    def output_menu(menu: str):
        # Display menu to user
        print(menu)
        print()  # extra space for UI appearance

    @staticmethod
    def input_menu_choice():
        """This function accepts user menu selection

        :return: string number as choice
        """
        choice = "0"
        try:
            choice = input("Please select an option: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose only 1, 2, 3, or 4")
        except Exception as e:
                IO.output_menu(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """This function prints student courses
        :param student_data: list of dictionaries as student data
        """
        print("-" * 50)
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} "
                  f"is enrolled in {student['CourseName']}")

    @staticmethod
    def output_error_message(message: str, error: Exception = None):
        """This function prints error message

        :param message: string message to display
        :param error: Exception to display
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def input_student_data(student_data: list):
        """This function accepts user input values and appends them to
        students list

        :param student_data: list of dictionaries as student data
        """
        try:
            #collect user inputs
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.strip():
                raise ValueError("The first name should not be empty.")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.strip():
                raise ValueError("The last name should not be empty.")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Enter the course's name: ")
            if not course_name.strip():
                raise ValueError("The course name should not be empty.")
            student_data_row = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student_data_row)
        except ValueError as e:
            IO.output_error_message(e.__str__())
        except Exception as e:
            IO.output_error_message("There was a non-specific error!", e)

#-- End of function definitions --#

#-- Beginning of the main body of script --#
# #Read data from file on initial start of program
# FileProcessor.read_data_from_file(FILE_NAME, [])
FileProcessor.read_data_from_file(file_name=FILE_NAME)

while True:

    #present menu
    IO.output_menu(menu=MENU)
    #store user selection and validate
    menu_choice = IO.input_menu_choice()

    #User input of student data
    if menu_choice == "1":
        IO.input_student_data(students)
        continue

    #Present current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    #save current data
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        continue

    #Stop the loop
    elif menu_choice == "4":
        break

print("End of Program.\nThank you!")
