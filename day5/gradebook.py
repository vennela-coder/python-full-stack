#main code
import gradefunction as gf

students = {}
print("\n STUDENT GRADEBOOK")

try:

    while True:
        print("\n1.add students along with marks")
        print("2.view  all students ")
        print("3.search student")
        print("4.update student details")
        print("5.remove student")
        print("6.exit")
        choice = int(input("Enter your choice :"))

        if choice==1:
            gf.add_student(students)
            
        elif choice==2:
            gf.view_all_student(students)

        elif choice==3:
            gf.search_student(students)


        elif choice==4:
            gf.update_marks(students)

        elif choice==5:
            gf.remove_student(students)

        
        else:
            print("exiting...")
            break

except Exception as error:
    print(f"error ocuured {error}") 

finally:
    print("DONE")