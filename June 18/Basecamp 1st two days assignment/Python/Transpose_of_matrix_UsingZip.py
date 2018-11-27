myList = [[1,2],[4,5], [3,7]]

for row in myList:
    print(row)
print("\n")
transMatrix= zip(*myList)
for row in transMatrix:
    print(row)
