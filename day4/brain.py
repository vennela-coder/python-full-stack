list=[2,4,5,6,8,9,11,14,20]
brain = 0
for i in range(0,len(list)):
    if list[i]>brain:

        brain=list[i]

print(f"{brain} is max")
