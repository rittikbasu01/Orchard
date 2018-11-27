marks=[]
n=int(input("How many Subjects:\n"))
 
for i in range(0,n):
    temp=int(input("Enter the marks:\n"))
    marks.append(temp)


print("Total Marks:" , sum(marks))
print("percentage:" , (sum(marks)/(n*100))*100)
        
