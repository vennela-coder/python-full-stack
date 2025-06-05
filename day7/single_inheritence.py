class Animal:
    def sound(self):
        print("bow bow bow")

    def eat(self):
        print("ammmm mmm mmm ...")  

    def jump(self):
        print("bukbukbuk") 


class Dog(Animal):

    def sounds(self):
        print("bowwwbowwboww")


class cat(Animal):
    def shout(self):
        print("meow meow meow")
        return "vennela"

class frog(Animal):
    def run(self):
        print("runnnnnnnnn")
    
    
x=Dog()
y=cat()
z=frog()
y.shout()
print(x.sound())
print(z.jump())