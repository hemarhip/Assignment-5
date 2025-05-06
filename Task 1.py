# Task 1: Create a Dictionary of Student Marks

Marks_dic = {'Alice':85, 'Nick':75, 'Emma':98, 'Alena':65}
Student_Name = input("Enter the student's name: ")
if Student_Name in Marks_dic:
    print(f"{Student_Name}'s marks: {Marks_dic[Student_Name]}")
else:
    print("Student not found.")