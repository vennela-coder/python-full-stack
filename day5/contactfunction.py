def add_contact(contacts):
    try:
        file=open("./sample.txt","a+")

        name=input("enter contact name: ")
        file.write(f"{name} : ")

        mobile=int(input("enter mobile: "))
        file.write(f"{mobile}")

        contacts[name]=mobile

        file=open("./sample.txt","a+")
        # file.write(f"{name} : {mobile}\n")
        # file.read()
        

    except Exception as e:
        print(f"invalid contact number{e}")

    finally:
        print("contact is added !!")
        file.close()

    


    
    
    
    
def view_contact(contacts):
    try:

        print("\n")

        for i in contacts:
            print(f"\n{i} : {contacts[i]}")

    except Exception as e:
        print(f"empty dictionary!!{e}")
            



def delete_contact(contacts):
    try:

        name_to_delete =input("enter name to delete: ")
        if name_to_delete in contacts:
            del contacts[name_to_delete]
            print(f"{name_to_delete} : contact  is removed")

    except Exception as e:
        print(f"error is {e}")


        

def find_contact(contacts):

    try:

        name_to_find=input("enter name to find: ")
        for name_to_find in contacts:
            if name_to_find in contacts:
                print("found")
            print(f"\n{name_to_find}:{contacts[name_to_find]}")

    except Exception as e:
        print(f"error ocuured!!")




def edit_contact(contacts):
    try:


        file=open("./sample.txt","a")

        name_to_edit=input("enter name to edit: ")
        # file.write(f"{name_to_edit}")

        
        

        file.close()

        file=open("./sample.txt","a")

        mobile=int(input("enter number to edit"))
        file.write(f"{mobile}  ")




        if contacts[name_to_edit] in contacts:

            del contacts[name_to_edit]

            contacts[name_to_edit]=mobile
            
            file.write(f"{contacts[name_to_edit]}")

            file.close()
            

    except Exception as e:
        print(f"error occured {e}")

    finally:

    # file.write(f"{number}")
        print("successfully done")
        
        file.close()


    


