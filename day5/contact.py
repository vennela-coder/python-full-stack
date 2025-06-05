import contactfunction as cf
contacts = {}
print("\n <=====CONTACTS APP=====>\n")


try:
    # file=open("./sample.txt","a")
    while True:

        print("\n1.add contact")
        print("2.view contact")
        print("3.delete contact")
        print("4.find contact")
        print("5.edit contact")
        print("6.exit")


        choice=int(input("enter your choice: "))

        if choice==1:
            cf.add_contact(contacts)

        elif choice==2:
            cf.view_contact(contacts)

        elif choice==3:
            cf.delete_contact(contacts)

        elif choice==4:
            cf.find_contact(contacts)

        elif choice==5:
            cf.edit_contact(contacts)

        else:
            print("Exiting.......")

            break

except Exception as error:
    print(f"error occured {error}")


finally:
    print("SUCCESSFULLY DONE")

    
    

    
    
    



    

    