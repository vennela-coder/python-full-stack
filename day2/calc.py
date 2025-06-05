op1=int(input("enter any number1"))
opr=input("Enter operator like + - * / : ")
op2=int(input("enter any number2"))


if opr == "+":
    a=op1+op2
    print(f"op1+op2={a}")

elif opr == "-":
    a=op1-op2
    print(f"op1-op2={a}")

elif opr=="*":
    a=op1*op2
    print(f"op1*op2={a}")

elif opr=="/":
    a=op1/op2
    print(f"op1/op2={a}")

else:
    print("enter correct opertor")




    
