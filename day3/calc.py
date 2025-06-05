#from arth import add
import arth as i

# main code

num1=int(input())
while True:
    op=input()

    if op=="=":
        print("end of the operation",num1)
        break

    num2=int(input())

    if op=="+":
        num1=i.add(num1,num2)

    elif op=="-":
        num1= i.sub(num1,num2)

    elif op=="*":
        num1= i.mul(num1,num2)

    elif op=="/":
        num1= i.div(num1,num2)

    elif op=="**":
        num1= i.pow(num1,num2)

    elif op=="%":
        num1= i.mod(num1,num2)

    print(num1)



