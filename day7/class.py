class movie:
    # hero=""
    # budget=0
    # tittle=""


    def __init__(self ,name,budget,tittle,year):
        self.hero=name
        self.budget=budget
        self.tittle=tittle
        self.year=year
        pass

    def display(self):
        print(f"{self.hero} is in {self.tittle} of {self.budget} budget in {self.year} year")
        pass

    def court(self):
        print(f"{self.budget} : {self.hero} : {self.year}")


movie_name=movie("yash",400000,"KGF7",1990)
movie_name2=movie("prabhas", 9000000,"bahubali",1998)
movie_name3=movie("ram",700000,"hit3",2005)
# movie_name.hero="yash"
# movie_name.budget=400000
# movie_name.tittle="KGF7"
# print(movie_name.budget)

# print(movie_name.hero)
# print(movie_name.budget)
# print(movie_name.tittle)
# print(movie_name.year)
print(movie_name.display())
print(movie_name2.court())
print(movie_name3.court())
print(movie_name3.display())
    
