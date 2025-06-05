from abc import ABC ,abstractmethod

class cricket(ABC):
    # file=open("./detail.txt","a")
    def __init__(self,name,balls,overs):
        self.batsman=name
        self.balls=balls
        self.overs=overs

    @abstractmethod
    def get_batsman(self):
        pass

    @abstractmethod
    def get_overs(self):
        pass

    @abstractmethod
    def get_balls(self):
        pass

    # file.close()

class score(cricket):
    # file=open("./detail.txt","a")

    def get_batsman(self):
        return f"BATSMAN : {self.batsman}"

    def get_balls(self):
        return f"TOTAL BALLS : {self.balls}"

    def get_overs(self):
       return f"OVERS COMPLETED : {self.overs}"

    # file.close()


class Details(cricket):
    # file=open("./detail.txt","a")

    def get_batsman(self):
        return f"BATSMAN : {self.batsman}"

    def get_balls(self):
        return f"TOTAL BALLS : {self.balls}"

    def get_overs(self):
        return f"OVERS COMPLETED : {self.overs}"

    # file.close()

ipl=score("MSD",20,6)
d=Details("virat",10,9)

with open("./detail.txt","a") as file:

    file.write("<==== SCORE ====>\n")
    file.write(" DETAILS \n\n")
    file.write(ipl.get_batsman())
    file.write("\n")
    file.write(ipl.get_balls())
    file.write("\n")
    file.write(ipl.get_overs())
    file.write("\n\n")
    file.write(d.get_batsman())
    file.write("\n")
    file.write(d.get_balls())
    file.write("\n")
    file.write(d.get_overs())
    file.close()

print(ipl.get_batsman())
print(ipl.get_balls())
print(ipl.get_overs())
print(d.get_batsman())
print(d.get_balls())
print(d.get_overs())