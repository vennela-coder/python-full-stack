my_list1=[10,20,30,40,50]
my_list2=[100,200,300,400,500]
my_list1.append(60)
my_list1.remove(20)
my_list2.pop(1)
my_list2.insert(2,100)
print(my_list1)

my_list1.extend(my_list2)
print(my_list1)
