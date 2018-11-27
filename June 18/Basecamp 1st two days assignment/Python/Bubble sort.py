def BubbleSort(arrList):
    for num in range(len(arrList)-1,0,-1):
        for i in range(num):
            if arrList[i]>arrList[i+1]:
                arrList[i],arrList[i+1] = arrList[i+1],arrList[i]

aList = [54,26,93,17,77,31,44,55,20]
BubbleSort(aList)
print(aList)
