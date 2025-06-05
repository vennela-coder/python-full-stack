def add_student(students):
    name=input("enter name of the student:")
    marks = list(map(int , input("Enter space seperated marks :").split(" ")))
    print(marks)
    students[name] = marks

def view_all_student(students):
    print("\n")
    for i in students:
        print(f"{i}:{students[i]} ")

def remove_student(students):
    name_to_delete=input("enter name to delete:")
    # for i in students:
    if name_to_delete in students:
        del students[name_to_delete]
        print(f"student {name_to_delete}  is removed")


def update_marks(students):
    name=input("enter student name for updation: ")
    if name in students:
        students[name]=list(map(int, input("enter marks to update").split(" ")))
        print("updated marks:",students[name])


def search_student(students):

    search_name=input("enter name to search : ")

    for search_name in students:
        
        if search_name in students:
           
            print("student found")
            break
    print(f"  {search_name} :",students[search_name])


