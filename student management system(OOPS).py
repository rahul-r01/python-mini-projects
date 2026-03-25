class StudentManagement:
    def __init__(self):
        self.students = {}  # {rollno: {"name": name, "marks": marks}}

    def add_student(self, name, rollno, marks):
        if rollno in self.students:
            print("\nRollno no is already exists!")
            return
        else:    
           self.students[rollno] = {"name": name, "marks": marks}
           print("\nStudent added successfully")
    def update_student(self,rollno):
        if rollno not in self.students:
            print("\nStudent not found!")
            return
        while True:
             print("What do you want to update?")
             print("1.NAME")
             print("2.MARKS")
             print("3.BOTH")
             print("4.EXIT")
             try:
                choice=int(input("Enter your choice: "))
             except ValueError:
                print("ValueError:Enter digits only!") 
                continue 
             if choice==1:
                new_name=input("Enter new name: ")
                self.students[rollno]['name']=new_name
                print("Name updated successfully!")
             elif choice==2:
                new_marks=int(input("Enter new marks: "))
                self.students[rollno]['marks']=new_marks
                print("Marks updated successfully!")
             elif choice==3:
                new_name=input("Enter new name: ")
                new_marks=int(input("Enter new marks: "))
                self.students[rollno]['name']=new_name
                self.students[rollno]['marks']=new_marks
                print("Name & Marks updated successfully!")
             elif choice==4:
                 print("Exiting..update menu!")
                 break
             else:
                print("Invalid choice...try again!")
                  
    
    def display_students(self):
        if not self.students:
            print("\nNo Students data exists!")
            return
        else:     
            print("\n***STUDENTS LIST***")
            print("_____________________")
            for rno, data in self.students.items():
                 print(f"name:{data['name']}, rollno:{rno}, marks:{data['marks']}")

    def delete_student(self, rollno):
        if rollno in self.students:
            del self.students[rollno]
            print(f"Student with rollno {rollno} deleted successfully!")
        else:
            print("Student not found!")
stud = StudentManagement()   # just once
print("*****STUDENT MANAGEMENT SYSTEM*****")
print("___________________________________")
while True:
    print("\nDESCRIPTION:")
    print("   1.ADD STUDENT DETAILS")
    print("   2.DISPLAY STUDENTS")
    print("   3.DELETE STUDENT")
    print("   4.MODIFY STUDENT DETAILS")
    print("   5.EXIT")
    try:
       choice=int(input("Enter a choice: "))
    except ValueError:
        print("ValueError: Enter digits only!")
        continue   
    if choice == 1:
        name=input("\nEnter a student name: ")
        rollno=input("Enter a student rollno: ")
        marks=int(input("Enter a student marks: "))
        stud.add_student(name, rollno, marks)
    elif choice == 2:
        stud.display_students()
    elif choice == 3:
        rno = input("\nEnter rollno to delete: ")
        stud.delete_student(rno)
    elif choice==4:
        rno=input("Enter roll no to update details: ")
        stud.update_student(rno)
    elif choice == 5:
        print("\nExiting..thank you!")
        break  
    else:
        print("\nInvalid choice..try again!")