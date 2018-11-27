myList = [[1,2],[4,5], [3,7]]

for row in myList:
    print(row)
rez = [[myList[j][i] for j in range(len(myList))] for i in range(len(myList[0]))]
print("\n")
for row in rez:
    print(row)
