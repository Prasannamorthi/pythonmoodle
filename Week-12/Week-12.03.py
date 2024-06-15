Background:

Dr. John Wesley maintains a spreadsheet with student records for academic evaluation. The spreadsheet contains various data fields including student IDs, marks, class names, and student names. The goal is to develop a system that can calculate the average marks of all students listed in the spreadsheet.



Problem Statement:

Create a Python-based solution that can parse input data representing a list of students with their respective marks and other details, and compute the average marks. The input may present these details in any order, so the solution must be adaptable to this variability.



Input Format:



The first line contains an integer N, the total number of students.

The second line lists column names in any order (ID, NAME, MARKS, CLASS).

The next N lines provide student data corresponding to the column headers.

Output Format:



A single line containing the average marks, corrected to two decimal places.

Constraints:



1≤N≤100

Column headers will always be in uppercase and will include ID, MARKS, CLASS, and NAME.

Marks will be non-negative integers.



For example:

Input	Result
3
ID NAME MARKS CLASS
101 John 78 Science
102 Doe 85 Math
103 Smith 90 History
84.33
3
MARKS CLASS NAME ID
78 Science John 101
85 Math Doe 102
90 History Smith 103
84.33
def calculate_average_marks(N, column_names, student_data):
    marks_index = column_names.index("MARKS")
    total_marks = 0
    valid_students_count = 0
   
    for student in student_data:
        if len(student) > marks_index and student[marks_index].isdigit():
            total_marks += int(student[marks_index])
            valid_students_count += 1
           
    if valid_students_count == 0:
        return 0  # No valid students with marks found
   
    average_marks = total_marks / valid_students_count
    return average_marks

if __name__ == "__main__":
    N = int(input())
    column_names = input().split()
    student_data = []
    for _ in range(N):
        student_info = input().split()
        student_data.append(student_info)
   
    average_marks = calculate_average_marks(N, column_names, student_data)
    print("{:.2f}".format(average_marks))

