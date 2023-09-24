# Switcher for implementing switch case options
def Student_details(ID):
    s = {
        "1004": "Student Name: MD. Mehrab, Department: CSE",
        "1009": "Student Name: Mita Rahman, Department: Mechanical",
        "1010": "Employee Name: Sakib Al Hasan,  Department: Electrical ",

    }
    
    return s.get(ID, "nothing")

# Take the student ID
ID = input("Enter the Student ID: ")
# Print the output
print(Student_details(ID))